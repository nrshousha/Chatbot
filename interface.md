
# `Interface.md`

## Overview

The `Interface` class provides a user-friendly command-line chatbot interface with human-like typing animations, fuzzy command handling, and basic system operations like clearing the chat and exiting the program.

This is not just a chatbot; it's a vibe—a retro terminal experience with a Gen Z twist. The bot thinks slowly, types dramatically, and even forgives your typos (thank you, `fuzzywuzzy`).

---

## ✨ Features

* Typing animation for a natural, human feel.
* Handles typos in commands using fuzzy matching.
* Colorful command-line interface (via `colorama`).
* Basic commands:

  * `/help`: Show available commands.
  * `/exit`: Quit the program.
  * `/clear`: Clear the chat session.
  * `/sysinfo`: Show system information (requires `system_info.py`).
* Threaded animations for bot typing simulation.
* Cross-platform terminal clearing (`Windows` & `Unix` compatible).

---

## 🔧 Dependencies

Make sure to install the following Python packages:

```bash
pip install colorama fuzzywuzzy python-Levenshtein
```

---

## 📚 Class Structure: `Interface`

### `__init__()`

* Initializes colorama.
* Sets up available commands.
* Initializes chat history.

---

### `type_effect(text, delay=0.03, end='\n')`

* Prints text with a typing animation.
* Parameters:

  * `text`: The string to display.
  * `delay`: Delay between characters.
  * `end`: End character (default: newline).

---

### `help()`, `show_help()`

* Displays available chatbot commands.

---

### `exit()`, `exit_chat()`

* Prints a goodbye message and exits the program gracefully using `sys.exit(0)`.

---

### `clear()`, `clear_chat()`

* Clears the terminal screen and resets the chat history.
* Works on both Windows (`cls`) and Unix (`clear`) systems.

---

### `get_user_input()`

* Prompts the user for input.
* Adds input to history.
* If input starts with `/`, it handles it as a command.
* Handles `KeyboardInterrupt` for a clean exit.

---

### `handle_command(command)`

* Uses fuzzy matching to allow typo-tolerant commands.
* Threshold for match: 70%.
* Executes the matching command or informs the user if unknown.

---

### `display_response(response)`

* Displays the bot’s response with typing animation.

---

### `run()`

* Starts the chatbot loop.
* Handles input, simulates bot thinking, and prints response.

---

### `bot_typing_animation()`

* Displays a "Bot is typing..." animation using dots and delays.

---

### `slow_print(text, delay=0.02)`

* Alternative to `type_effect`, prints slowly without coloring.

---

## 📁 Related Files

* `threads.py`: Must contain `threadFN`, but it's not used in this snippet. Placeholder for future features?
* `system_info.py`: Expected to have a `display_system_info()` method to be invoked via `/sysinfo`.

---

## 🧠 Pro Tips

* Add your own bot logic in `display_response()` or extend `run()` to integrate NLP or API calls.
* You could even replace the hardcoded `You said: {user_input}` with something smarter.

---

## 💥 Example Usage

```bash
python interface.py
```

Then interact via the terminal:

```
You: /help
You: /clear
You: hellp  <-- still works thanks to fuzzy logic!
You: /exit
```

---

## 🎯 Future Improvements (Ideas)

* Integrate OpenAI API for smarter responses.
* Add chat logging to file.
* Create a GUI version using Tkinter or PyQt.
* Emoji support? Why not 🤖✨

---
