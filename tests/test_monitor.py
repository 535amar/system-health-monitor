import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def run_bash_script():
    result = subprocess.run(
    ["bash", "./bash_scripts/collect_stats.sh"],
    capture_output=True,
    text=True
    
    )
    return result.stdout

def main():
    print(Fore.CYAN + Style.BRIGHT + "============SYSTEM HEALTH MONITOR==========")
    stats = run_bash_script()
    print(Fore.GREEN + stats)

if __name__ == "__main__":
    main() 