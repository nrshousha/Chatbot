import time
# we will use it in creating more natural << humanely >> chatbot
import sys
# imortant for handling system like exit
import os
# used for operating system interaction like clearing the terminal 
from colorama import Fore, Style, init
from fuzzywuzzy import process
import threading
#handles mistyped commands 
from threads import threadFN

class Interface():

    def __init__(self):
        init()  # to init the colorama
        self.chat_history = [] 
        self.commands = {
            "/help": self.help,
            "/exit": self.exit,
            '/clear': self.clear
        }

    def type_effect(self, text, delay=0.03, end='\n'):
        # methode for the typing animation 
        for char in text:
            sys.stdout.write(char)# prints one character at a time
            sys.stdout.flush()# displays the character 
            time.sleep(delay)# delays between each character
        if end:
            print(end, end='') 
        
    def help(self):
        self.show_help()  # calls for the show help 
    
    def show_help(self):
        help_text = f"\n{Fore.GREEN}Available commands:{Style.RESET_ALL}"
        help_text += f"\n{Fore.MAGENTA}/help{Style.RESET_ALL} \n"
        help_text += f"\n{Fore.MAGENTA}/exit{Style.RESET_ALL} - Quit the program\n"
        help_text += f"\n{Fore.MAGENTA}/clear{Style.RESET_ALL} - Clear chat\n"
        # Style.RESET_ALL this stops bleeding between each color and style
        self.type_effect(help_text) 

    def exit(self):
        print("Exiting the program.")
        self.exit_chat()  # calls for the exit 

    def exit_chat(self):
        self.type_effect(f"{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
        sys.exit(0)

    def clear(self):
        self.type_effect(f"\n{Fore.BLUE}Clearing chat data...{Style.RESET_ALL}")
        self.clear_chat()  # calls the clear method 
    
    def clear_chat(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        # this make it compatible with all operating systems windows or Linux 
        # windows would write cls and linux clear 

        self.chat_history = []
        self.type_effect(f"{Fore.GREEN}Chat cleared successfully!{Style.RESET_ALL}")
        self.type_effect(f"{Fore.CYAN}New chat session started.{Style.RESET_ALL}\n")
    
    def get_user_input(self):
        try:
            user_input = input(f"{Fore.CYAN}You:{Style.RESET_ALL} ").strip()
            self.chat_history.append(user_input)
            # handle commands
            if user_input.startswith('/'):
                self.handle_command(user_input)
                return None
                
            return user_input # pass it to the chatbot 

        except KeyboardInterrupt:
            self.exit_chat()
    
    def handle_command(self, command):
        matches = process.extractOne(command, self.commands.keys()) 
        # uses fuzzy to handle 
        # where function will compare the input to all commands 
        if matches[1] > 70:  # 70% similarity threshold
            self.commands[matches[0]]()
            # this finds the matched command and calls it 
        elif command == "/sysinfo":
            import system_info
            system_info.display_system_info()
        else:
            self.type_effect(f"{Fore.RED}Unknown command. Type /help for options.{Style.RESET_ALL}")
            
    def display_response(self, response):
        print(f"{Fore.MAGENTA}Bot:{Style.RESET_ALL} ", end="")  # no newline
        self.type_effect(response)


    def run(self):
        self.type_effect(f"{Fore.GREEN}Chat started. Type /help for commands.{Style.RESET_ALL}")
        while True:# infinite loop 
            user_input = self.get_user_input()
            if user_input:
                # Start the typing animation in a separate thread
                typing_thread = threading.Thread(target=self.bot_typing_animation)
                typing_thread.start()

                # Simulate response generation delay
                time.sleep(1.2)  # <-- this is your fake "thinking" time

                # Wait for the animation thread to finish
                typing_thread.join()

                # Finally, print the bot's actual response
                self.display_response(f"You said: {user_input}")


    def bot_typing_animation(self):
        print(f"{Fore.MAGENTA}Bot:{Style.RESET_ALL} ", end="", flush=True)
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.4)
        print("\r" + " " * 20 + "\r", end="", flush=True)

    def slow_print(self, text, delay=0.02):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

if __name__ == "__main__":
    chat = Interface()
    chat.run()  # starts the chat 
