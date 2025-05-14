import psutil
import platform
import os
import time

# Function to get CPU usage
def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

# Function to get memory details
def get_memory_info():
    mem = psutil.virtual_memory()
    return f"Memory - Total: {mem.total // (1024**3)} GB, Used: {mem.used // (1024**3)} GB, Free: {mem.available // (1024**3)} GB"

# Function to get uptime
def get_system_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = uptime_seconds // 3600
    uptime_minutes = (uptime_seconds % 3600) // 60
    return f"Uptime: {int(uptime_hours)} hours, {int(uptime_minutes)} minutes"

# Function to get disk usage
def get_disk_usage():
    disk = psutil.disk_usage("C:\\")
    return f"Disk Usage - Total: {disk.total // (1024**3)} GB, Used: {disk.used // (1024**3)} GB, Free: {disk.free // (1024**3)} GB"

# Function to check system load and suggest breaks
def check_system_load():
    cpu_load = psutil.cpu_percent(interval=1)
    mem_load = psutil.virtual_memory().percent
    
    if cpu_load > 80 or mem_load > 85:
        return f"🚨 High system load detected! CPU: {cpu_load}%, Memory: {mem_load}% - Consider taking a break! 🚀"
    else:
        return f"System load is normal. CPU: {cpu_load}%, Memory: {mem_load}%"

# Function to display all system info
def display_system_info():
    print(get_cpu_usage())
    print(get_memory_info())
    print(get_system_uptime())
    print(get_disk_usage())
    print(check_system_load())

# Run the system info check
if __name__ == "__main__":
    display_system_info()