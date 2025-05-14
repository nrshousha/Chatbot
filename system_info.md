
# 🖥️ `System Diagnostics Module`

This module provides real-time information about your system's performance. It's used in the chatbot client to respond to `/sysinfo` commands, giving a snapshot of CPU, memory, disk usage, uptime, and system load.

---

## 📦 Features

* ✅ CPU usage (percent)
* ✅ Memory stats (total, used, free)
* ✅ Disk usage on drive `C:\` (can be customized)
* ✅ System uptime in hours and minutes
* ✅ Load monitoring (alerts if CPU or RAM is too high)
* ✅ Command-line compatible (`python system_info.py`)

---

## 🔧 Dependencies

* [`psutil`](https://pypi.org/project/psutil/)
* `platform` (optional, standard library)
* `os` (standard library)
* `time` (standard library)

Install with:

```bash
pip install psutil
```

---

## 🧩 Functions Overview

### `get_cpu_usage()`

Returns the current CPU usage over a 1-second sample:

```python
"CPU Usage: 27%"
```

---

### `get_memory_info()`

Reports total, used, and free RAM in gigabytes:

```python
"Memory - Total: 16 GB, Used: 8 GB, Free: 7 GB"
```

---

### `get_system_uptime()`

Calculates uptime since last boot:

```python
"Uptime: 3 hours, 45 minutes"
```

---

### `get_disk_usage()`

Reports disk usage on the system's C:\ drive (Windows):

```python
"Disk Usage - Total: 500 GB, Used: 320 GB, Free: 180 GB"
```

> 📝 On Linux/macOS, change the drive path to `'/'` or use `os.path.abspath(os.sep)` for compatibility.

---

### `check_system_load()`

Returns a performance health check:

Normal:

```python
"System load is normal. CPU: 25%, Memory: 50%"
```

High load:

```python
"🚨 High system load detected! CPU: 91%, Memory: 89% - Consider taking a break! 🚀"
```

---

### `display_system_info()`

Calls all of the above and prints them line-by-line. Used when:

```bash
python system_info.py
```

---

## ⚙️ Usage in the Chat Client

When the user types `/sysinfo`, the client imports and runs this module to give the user an overview of their system's health during the chat session.

---

## ✅ Example Output

```
CPU Usage: 18%
Memory - Total: 16 GB, Used: 7 GB, Free: 9 GB
Uptime: 5 hours, 22 minutes
Disk Usage - Total: 512 GB, Used: 410 GB, Free: 102 GB
System load is normal. CPU: 18%, Memory: 44%
```

---

## 🚀 Future Improvements

* Add platform/OS info via `platform.system()`, `platform.release()`
* Add CPU temperature stats (if supported)
* Cross-platform disk support

---

