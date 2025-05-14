
# `Chat Server Documentation`

This file implements the **TCP server** for the chatbot application. It listens for incoming client connections, prompts each user to choose a chatbot "mood", and continuously handles user input using threaded communication.

---

## 📜 Features

* **Socket Server** using Python's `socket` module
* **Multithreaded** client handling (`threading.Thread`)
* **AI Response Engine** (via `ai_engine.get_ai_response`)
* **Mood-based Conversation** (e.g., sarcastic, serious)
* **Graceful Client Disconnection**

---

## 🚀 How It Works

1. Starts a TCP server listening on `127.0.0.1:65432`
2. Accepts incoming client connections
3. Prompts each client to select a **chatbot mood**
4. Handles each client in a separate thread
5. Reads messages from the client and responds using the AI engine
6. Closes the connection when the client disconnects

---

## 🧠 Mood Support

Clients are prompted to select one of the following chatbot moods:

* `default`
* `sarcastic`
* `enthusiastic`
* `serious`

Mood affects how the chatbot phrases its response. The chosen mood is passed to the AI response generator.

---

## 🧩 Main Components

### `handle_client(conn, addr)`

* Manages the full lifecycle of a single client connection
* Prompts for mood → receives messages → sends AI responses
* Ends when the client disconnects

### `main()`

* Starts the TCP socket server
* Waits for client connections
* Spawns a new thread for each incoming client

---

## 🔄 Communication Flow

```text
Client connects
 └──> Server sends mood prompt
     └──> Client replies with mood
         └──> Server validates mood
             └──> Server enters chat loop:
                 └──> Client sends message
                     └──> Server uses AI to respond
```

---

## 🛠️ Code Flow (Detailed)

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
```

* Sets up a TCP socket on localhost, port 65432.

```python
conn, addr = s.accept()
thread = threading.Thread(target=handle_client, args=(conn, addr))
thread.start()
```

* Accepts new clients and handles each in a separate thread for scalability.

```python
mood = conn.recv(1024).decode().strip().lower()
```

* Receives the mood input and checks it against a list of allowed moods.

```python
response = ai_engine.get_ai_response(user_input, mood=mood)
conn.sendall(response.encode('utf-8'))
```

* Gets a response from the AI and sends it back to the client.

---

## 📁 Dependencies

| Module      | Role                                                   |
| ----------- | ------------------------------------------------------ |
| `socket`    | Low-level network communication                        |
| `threading` | Allows handling multiple clients                       |
| `ai_engine` | External module that generates responses based on mood |

---

## 🧪 Sample Console Output

```
[SERVER] Listening on 127.0.0.1:65432
[+] New connection from ('127.0.0.1', 50522)
[Client ('127.0.0.1', 50522)] selected mood: sarcastic
[LOG] Generated response: Wow, another genius question. How original.
```

---

## ✅ To-Do / Suggestions

* [ ] Add logging of user messages for moderation or analytics
* [ ] Add connection timeout handling
* [ ] Broadcast mode (group chat)
* [ ] Secure communication with SSL
* [ ] External config file for HOST/PORT

---
