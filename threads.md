
### 📄 `threads module documentation`

# 🧵 `threads.py` – Thread-Safe Printing & Async Logging

This module provides thread-safe utilities to ensure clean console output and non-blocking logging in a multithreaded chat client environment.

---

## 🔧 Purpose

In multithreaded applications like your chatbot client, multiple threads may try to print or log simultaneously. This can lead to:

* **Jumbled console output**
* **Laggy user experience** due to blocking log operations

The `threadFN()` function in this file returns two tools to solve those problems:

* `safe_print()` — Ensures clean, thread-safe printing.
* `async_log()` — Logs messages in the background without blocking the chat flow.

---

## 📦 Function: `threadFN()`

```python
def threadFN():
    print_lock = threading.Lock()

    def safe_print(message):
        with print_lock:
            print(message)

    def async_log(user_input, bot_response):
        threading.Thread(target=log_message, args=(user_input, bot_response)).start()

    return safe_print, async_log
```

---

### 🔐 `print_lock = threading.Lock()`

* Prevents **race conditions** in terminal output.
* Only one thread can print at a time.

---

### 🖨️ `safe_print(message)`

* Ensures that messages printed by different threads **don’t overlap**.
* Example usage:

  ```python
  safe_print("Bot: Thinking...")
  ```

---

### 📝 `async_log(user_input, bot_response)`

* Starts a new **background thread** to write logs using `logger.log_message()`.
* Prevents UI freezing or delays when writing to a file.
* Example usage:

  ```python
  async_log("hello", "Hi there!")
  ```

---

### ✅ Return

`threadFN()` returns both functions:

```python
safe_print, async_log = threadFN()
```

Now, you can use `safe_print()` and `async_log()` anywhere in your chat client for:

* Clean terminal output
* Smooth, non-blocking session logging

---

## 📎 Where It's Used

In `client.py`:

```python
from threads import threadFN

safe_print, async_log = threadFN()
```

These are used to:

* Print bot messages without clutter
* Log user/bot messages in the background

---

## 🧠 Summary

| Function     | Purpose                                        |
| ------------ | ---------------------------------------------- |
| `safe_print` | Prevents print conflicts from multiple threads |
| `async_log`  | Logs in the background without UI lag          |

The `threads.py` module improves the chatbot’s user experience by making its output and logging **clean**, **fast**, and **thread-safe**.

---
