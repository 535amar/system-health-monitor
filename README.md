# 🖥️ System Health Monitor

A simple yet powerful **System Health Monitor** built with **Python** and **Bash**.  
It collects system stats (CPU, RAM, Disk, and Network usage) using a Bash script and displays them with a clean, colored output in Python.

---

## 📌 Features
-  CPU load averages  
-  RAM usage (used/total with percentage)  
-  Disk usage (used/total with percentage)  
-  Network stats (packets sent/received)  
-  Colored, easy-to-read terminal output  
-  Cross-platform script execution using `subprocess`  

---

## 🚀 Project Structure
system-health-monitor/
│── monitor.py # Main Python script
│── bash_scripts/
│ └── collect_stats.sh # Bash script to collect system stats
│── venv/ # (optional) Virtual environment

----------------------------------------

## ⚡ Installation & Usage

### 1. Clone the repo

git clone https://github.com/535amar/system-health-monitorgit
cd system-health-monitor
### 2.Run the monitor
python3 monitor. py

## 📦 Dependencies
. [python.3.x](https://www.python.org)
. [colorama](https://pypi.org/project/colorama)


## 📌 Future Improvements
. Add logging support (save stats to file)
. Add real-time monitoring with refresh option
. Create system alerts for high CPU/RAM usage
. Add Windows support
## Auther
[535amar](https://github.com/535amar)


okay ! Feel free to fork,contribute, or suggest improvements !