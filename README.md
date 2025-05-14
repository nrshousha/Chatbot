# 🤖 Chatbot

A terminal-based chatbot application designed to simulate human-like conversations. Built with Python, it features a modular architecture, command handling, system information retrieval, and threaded operations for enhanced performance.

---

## 📋 Table of Contents

* [Features](#features)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)

---

## 🚀 Features

* **Interactive Chat Interface**: Engages users in a conversational manner through the terminal.
* **Command Handling**: Supports commands like `/help`, `/exit`, `/clear`, and `/sysinfo`.
* **System Information Retrieval**: Displays CPU usage, memory details, disk usage, and system uptime.
* **Threaded Operations**: Utilizes threading for non-blocking logging and smooth user experience.
* **Modular Design**: Organized codebase with separate modules for interface, logging, system info, and more.

---

## 🛠️ Getting Started

### Prerequisites

Ensure you have the following installed:

* Python 3.6 or higher
* `pip` package manager

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nrshousha/Chatbot.git
   cd Chatbot
   ```

2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` is not present, manually install the dependencies:*

   ```bash
   pip install colorama fuzzywuzzy python-Levenshtein
   ```

---

## 💡 Usage

1. **Start the server:**

   ```bash
   python server.py
   ```

2. **Run the client:**

   In a new terminal window:

   ```bash
   python client.py
   ```

3. **Interact with the chatbot:**

   * Type messages to converse.
   * Use commands:

     * `/help`: Display available commands.
     * `/exit`: Exit the chat.
     * `/clear`: Clear the chat history.
     * `/sysinfo`: Display system information.

---

## 📁 Project Structure

```
Chatbot/
├── ai_engine.py         # Handles AI response generation
├── client.py            # Client-side script for user interaction
├── interface.py         # Manages user interface and command handling
├── logger.py            # Logs chat history and system events
├── server.py            # Server-side script to manage connections
├── system_info.py       # Retrieves and displays system information
├── threads.py           # Implements thread-safe operations
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance the chatbot, fix bugs, or add new features:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and includes relevant tests.

---
