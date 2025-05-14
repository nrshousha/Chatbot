
# 📚 `libraries.md`

This file explains all external and internal libraries used in the chatbot project, including their purpose and how they contribute to the system’s overall functionality.

---

### 1. **Socket**

* **Purpose:** Used for setting up server–client communication in the chatbot as it enables TCP/IP protocols.

---

### 2. **Threading / Lock**

* **Purpose of `threading` library:** Allows the chatbot server to handle **multiple clients at once** by enabling multithreading.
* **Purpose of `Lock`:** Prevents race conditions when multiple threads are accessing shared resources simultaneously by using thread locks.

---

### 3. **OS**

* **Purpose:** Provides tools to interact with the operating system — e.g., clearing the terminal or fetching environment variables.

---

### 4. **Dotenv**

* **Purpose:** Loads environment variables from a `.env` file (like API keys), allowing sensitive data to be kept **outside** the main codebase.

---

### 5. **Time**

* **Purpose:** Enables time-based functions like `sleep()` for delay or timeout handling.

---

### 6. **Sys**

* **Purpose:** Lets the code interact with the Python runtime — especially for **safely exiting** the program (`sys.exit()`).

---

### 7. **Colorama**

* **Purpose:** Adds **color and style** to the terminal output, making the chatbot’s responses more visually appealing (like blue and magenta responses).

---

### 8. **Fuzzywuzzy**

* **Purpose:** Helps the chatbot understand **mistyped or approximate commands** using fuzzy string matching, improving user experience with imprecise inputs.

---

### 9. **JSON**

* **Purpose:** Handles **reading/writing** of chat logs and structured data in JSON format — essential for saving conversations.

---

### 10. **Datetime**

* **Purpose:** Provides access to the current date and time — used for **session tracking and logging**.

---

### 11. **Argparse**

* **Purpose:** Allows the chatbot to run with different **terminal configurations** by parsing command-line arguments.

---

### 12. **Psutil**

* **Purpose:** Retrieves **real-time system information** (CPU usage, memory, users, etc.) to support diagnostics or performance display.

---

### 13. **Platform**

* **Purpose:** Fetches detailed **OS info** — useful for logging system specifications and ensuring compatibility.
