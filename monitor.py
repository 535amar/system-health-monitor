import subprocess
import os
from colorama import Fore, Style, init

init(autoreset=True)

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "bash_scripts", "collect_stats.sh")
def run_bash_script():
    result = subprocess.run(
    ["bash", SCRIPT_PATH],
    capture_output=True,
    text=True
    
    )
    if result.stderr:
        print("Error:", result.stderr)
    return result.stdout

def main():
    print(Fore.CYAN + Style.BRIGHT + "============SYSTEM HEALTH MONITOR==========")
    stats = run_bash_script()
    print(Fore.GREEN + stats)

if __name__ == "__main__":
    main() 