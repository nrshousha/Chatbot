# client.py

import socket
import argparse
from interface import Interface
import logger
import system_info
import threading
from threads import threadFN
safe_print, async_log = threadFN()  # unpack the tools

HOST = '127.0.0.1'  # server's hostname or IP address
PORT = 65432        # The port used by the server

# parses terminal arguments like --debug and --log
def parse_args():
    parser = argparse.ArgumentParser()  # creates a parser object
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")  # adds --debug flag
    parser.add_argument("--log", action="store_true", help="Log the session")      # adds --log flag
    return parser.parse_args()  # returns parsed arguments

# Handles special commands manually (like /sysinfo)
def other_command(user_input):
    if user_input.strip() == "/sysinfo":
        system_info.display_system_info()
        return True
    return False

def main():
    args = parse_args()  # read terminal arguments like --debug or --log

    if args.debug:
        safe_print("Debug mode is enabled.") 
    if args.log:
        safe_print("Logging is turned on.") 

    ui = Interface()  # object to handle user interaction

    # Connect to the server socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # connect to server at specified HOST and PORT
        safe_print(f"[CLIENT] Connected to server at {HOST}:{PORT}")

        # 🌟 Receive mood prompt from server
        mood_prompt = s.recv(1024).decode('utf-8')  # receive the mood question from server
        print(f"{mood_prompt}", end='')  # display prompt to user
        mood = input().strip()  # get user mood input
        s.sendall(mood.encode('utf-8'))  # send mood to server

        while True:
            try:
                user_input = ui.get_user_input()  # get user input from Interface

                # skip if input was a built-in command like /exit
                if user_input is None:
                    continue

                # if input starts with /, it might be a command (like /sysinfo)
                if other_command(user_input):
                    continue  # skip sending to server if it's a special command

                # Send the user input to the server
                s.sendall(user_input.encode('utf-8'))

                # # Receive the chatbot response from the server
                # response = s.recv(1024).decode('utf-8')
                # # runs the tyoing animation 
                # Interface.bot_typing_animation()
                # # Properly simulate bot typing, then print response cleanly
                # # Animate and show bot response
                # # print(f"{Fore.MAGENTA}Bot:{Style.RESET_ALL} ", end="")
                # ui.slow_print(response)

                # Start bot typing animation in a thread
                typing_thread = threading.Thread(target=ui.bot_typing_animation)
                typing_thread.start()

                # Get response (while animation runs)
                response = s.recv(1024).decode('utf-8')

                # Wait for animation to finish (approx 1.2s)
                typing_thread.join()

                # Clean line and print response on same line
                print("\r", end="")  # overwrite 'Bot: ...'
                ui.display_response(response)




                # Save user input and server (bot) response in the log
                logger.log_message("user", user_input)
                ui.bot_typing_animation()
                logger.log_message("bot", response)
                # logger.show_recent_logs(10)  # show last 10 lines from log

            except KeyboardInterrupt:
                ui.exit_chat()  # exit if Ctrl+C is pressed
                break
            except Exception as e:
                safe_print(f"Error: {e}")  # catch any errors
                if args.debug:
                    import traceback
                    traceback.print_exc()  # print full error if in debug mode

if __name__ == "__main__":
    main()
