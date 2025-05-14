# server.py 

import socket # let us create a network connection using TCP/IP protocols 
import threading # this gives the server the privilege to handle multiple clients 
import ai_engine

HOST = '127.0.0.1' # set the sever to the localhost << so only accept connection on the same machine>>
PORT = 65432 

def handle_client(conn, addr):
    # addr is the ip + port of the clients 
    # conn is the socket connection
    print(f"[+] New connection from {addr}")
    # alert by printing a message that a client has connected 
    with conn:
        # this ask client for desired mood
        conn.sendall("Welcome! What mood should the chatbot use? (e.g., default, sarcastic, friendly): ".encode('utf-8'))
        mood = conn.recv(1024).decode('utf-8').strip() # decode('utf-8')--> converts text to binary 
        print(f"[Client {addr}] selected mood: {mood}")
        # server logs the mood 
        while True: # a loop that keeps receiving messages from client 
            data = conn.recv(1024)
            # data = conn.recv(1024).decode('utf-8')
            if not data:
                break #client disconnects
            user_input = data.decode('utf-8')

            # respond using selected mood
            response = ai_engine.get_ai_response(user_input, mood=mood)
            print(f"[LOG] Generated response: {response}")  
            conn.sendall(response.encode('utf-8'))
            # sends the response to the client 

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # AF_INET: this tells Python we're using IPv4 addresses
        s.bind((HOST, PORT))
        # instruct the server to listen on 127.0.0.1:65432.
        s.listen()
        print(f"[SERVER] Listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            #server waits for a client to connect
            #accept() -- > returns a new socket when a new connection a made 
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            # this allow the server to run a client in parallel for it to go and be ready to accept a new client 
if __name__ == "__main__":
    main()
