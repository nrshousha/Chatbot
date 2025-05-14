
# Logger module documentation

This module provides a simple and thread-safe mechanism to log messages (such as user input, bot responses, and error messages) to a session-specific JSON log file, with utilities to display recent logs and export them to a text file.

## 📁 File Structure and Setup

* **Log Directory**: All logs are saved under a `logs/` directory in the current working directory.
* **Log Filename**: Each session creates a new log file named using the current timestamp (e.g., `log_20250514_152301.json`).

---

## 📌 Functions

### `log_message(role: str, message: str)`

Logs a message with the specified role.

#### Parameters:

* `role` (`str`): The origin of the message (e.g., `"user"`, `"bot"`, `"error"`).
* `message` (`str`): The content of the message to log.

#### Example:

```python
log_message("user", "Hello!")
```

---

### `show_recent_logs(lines=10)`

Displays the most recent log entries from the current session’s log file.

#### Parameters:

* `lines` (`int`, optional): Number of recent lines to display. Defaults to 10.

#### Example:

```python
show_recent_logs(5)
```

#### Output:

```
[2025-05-14T15:23:01.123456] USER: Hello!
[2025-05-14T15:23:02.789012] BOT: Hi there!
...
```

---

### `export_log_to_txt(txt_path=None)`

Exports the current JSON log file to a plain-text `.txt` file for easier reading or archiving.

#### Parameters:

* `txt_path` (`str`, optional): Custom path for the exported file. If not provided, a `.txt` version of the current log file is created automatically.

#### Example:

```python
export_log_to_txt()
# or
export_log_to_txt("my_custom_log.txt")
```

#### Output:

```
✅ Log exported to logs/log_20250514_152301.txt
```

---

## 🔒 Thread Safety

* All write operations to the log file are wrapped in a `threading.Lock` to ensure thread safety when accessed from multiple threads concurrently.

---

## 📦 Dependencies

* Standard Python modules only:

  * `os`
  * `json`
  * `datetime`
  * `threading`

---

## ✅ Use Case

Ideal for chatbots, CLI tools, or any application where keeping a structured log of session messages is important for debugging, auditing, or reviewing interactions.

---

## 🛠 Future Enhancements

* Add log rotation or maximum file size enforcement.
* Include log levels (info, warning, error).
* Add support for logging to remote servers or databases.

---
