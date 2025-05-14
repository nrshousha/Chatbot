import os
import json
from datetime import datetime
from threading import Lock

# Lock to ensure thread-safe writing to the log file
log_lock = Lock()

LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# File name based on current session timestamp
session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_path = os.path.join(LOG_DIR, f"log_{session_id}.json")


def log_message(role: str, message: str):
    """Log a single message (user/bot/error) to the JSON file."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "message": message
    }

    with log_lock:
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def show_recent_logs(lines=10):
    """Display the last X lines from the current log file."""
    if not os.path.exists(log_file_path):
        print("⚠️ No logs available yet.")
        return

    with open(log_file_path, "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        recent = all_lines[-lines:]
        for line in recent:
            entry = json.loads(line)
            timestamp = entry["timestamp"]
            role = entry["role"]
            msg = entry["message"]
            print(f"[{timestamp}] {role.upper()}: {msg}")


def export_log_to_txt(txt_path=None):
    """Export the current JSON log to a simple TXT file."""
    if not os.path.exists(log_file_path):
        print("⚠️ No logs to export.")
        return

    if not txt_path:
        txt_path = log_file_path.replace(".json", ".txt")

    with open(log_file_path, "r", encoding="utf-8") as f_in, open(txt_path, "w", encoding="utf-8") as f_out:
        for line in f_in:
            entry = json.loads(line)
            f_out.write(f"{entry['timestamp']} - {entry['role']}: {entry['message']}\n")

    print(f"✅ Log exported to {txt_path}")
