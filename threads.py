# threads.py
import threading
from logger import log_message

def threadFN():
    # Lock to make prints/logs thread-safe
    print_lock = threading.Lock()

    def safe_print(message):
        with print_lock:
            print(message)

    def async_log(role, message):
        threading.Thread(target=log_message, args=(role, message)).start()

    return safe_print, async_log
