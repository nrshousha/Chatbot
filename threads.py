# threads.py
import threading
import time
from logger import log_message
from ai_engine import get_ai_response  # Make sure this is the right import

def threadFN():
    # Lock to make prints/logs thread-safe
    print_lock = threading.Lock()

    # Thread-safe print
    def safe_print(message):
        with print_lock:
            print(message)


    # Asynchronous logging (non-blocking log write)
    def async_log(user_input, bot_response):
        threading.Thread(target=log_message, args=(user_input, bot_response)).start()
