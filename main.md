
# `Chat Client Main Logic`

This file is the **main entry point** for the chat application's client-side logic. It connects to the server over TCP, handles user input, and displays chatbot responses, with support for logging, debug output, and built-in commands like `/sysinfo`.

---

## 📜 Features

* **Socket Communication**: Connects to the server using TCP.
* **User Interface Layer**: Clean interaction via a custom `Interface` class.
* **Typing Animation**: Simulates bot "thinking" using threading.
* **Session Logging**: Optionally logs messages to a `.json` file.
* **System Commands**: Supports commands like `/sysinfo` locally.
* **Command-Line Arguments**: Enables `--debug` and `--log` options.

---

## 🧪 Usage

```bash
python client.py [--debug] [--log]
```

| Flag      | Description                       |
| --------- | --------------------------------- |
| `--debug` | Enables detailed error tracebacks |
| `--log`   | Logs all messages to a JSON file  |

---

## 🧩 Code Structure

### `parse_args()`

Parses CLI arguments for debugging and logging.

### `Interface`

A helper class for managing:

* User input
* Typing animations
* Clean output
* Chat exit logic

### `logger`

A module that logs messages as timestamped JSON entries, and can export them as readable text.

### `system_info`

Handles `/sysinfo` command by displaying local system details without involving the server.

---

## 🔁 Main Chat Loop

1. Connects to the server (`HOST` and `PORT`).
2. Receives and responds to a **mood check prompt**.
3. Repeats:

   * Gets user input
   * Handles built-in commands (e.g., `/sysinfo`)
   * Sends input to server
   * Simulates typing animation
   * Receives and displays server response
   * Logs the messages if logging is enabled

---

## 🛑 Graceful Exit & Error Handling

* Handles `Ctrl+C` with a clean exit message.
* Shows full tracebacks if `--debug` is used.
* Catches and prints unexpected exceptions.

---

## 📁 Related Files

| File             | Role                        |
| ---------------- | --------------------------- |
| `interface.py`   | UI handling (input/output)  |
| `logger.py`      | Message logging to file     |
| `system_info.py` | Built-in command support    |
| `server.py`      | The server-side counterpart |

---

## ✅ Example Output

```
[CLIENT] Connected to server at 127.0.0.1:65432
How are you feeling today? > good
> Hello!
Bot is typing...
Bot: Nice to hear that! How can I help you?
```
