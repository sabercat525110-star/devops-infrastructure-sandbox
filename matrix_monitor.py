import os
import time
import psutil
from colorama import init, Fore, Style

# Initialize color palette for Windows 11 terminal
init(convert=True)

# Neon Purple and Lightning Yellow palette
HEADER = Fore.MAGENTA + Style.BRIGHT   
DATA = Fore.YELLOW + Style.BRIGHT     
ALERT = Fore.RED + Style.BRIGHT        
RESET = Style.RESET_ALL

def get_bar_graph(percentage):
    """Generates a dynamic 20-character visual progress bar."""
    blocks = int(round(percentage / 5))
    return DATA + "█" * blocks + Fore.WHITE + "░" * (20 - blocks)

def run_dashboard():
    try:
        while True:
            # Clear the terminal window cleanly every refresh cycle
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Fetch raw real-time system metrics
            cpu_usage = psutil.cpu_percent(interval=None)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            print(HEADER + "==================================================")
            print("🚀 VORPHIX SYSTEM HARDWARE TELEMETRY MATRIX 🚀")
            print("==================================================" + RESET)
            
            # CPU Metrics
            print(f"\n[🔥 CPU COMPILING STATUS]")
            print(f"Usage Metrics : {cpu_usage}%")
            print(f"Core Activity : [{get_bar_graph(cpu_usage)}{RESET}]")
            
            # Memory Metrics
            print(f"\n[🧠 DDR5 RAM MATRIX]")
            print(f"Memory Loaded : {memory.percent}% ({round(memory.used / (1024**3), 2)} GB / {round(memory.total / (1024**3), 2)} GB)")
            print(f"Buffer Status : [{get_bar_graph(memory.percent)}{RESET}]")
            
            # Storage Metrics
            print(f"\n[💽 SYSTEM SSD MATRIX]")
            print(f"Disk Capacity : {disk.percent}% Used ({round(disk.free / (1024**3), 2)} GB Free)")
            print(f"Space Ledger  : [{get_bar_graph(disk.percent)}{RESET}]")
            
            # Safety Alert Trigger Threshold
            if cpu_usage > 85 or memory.percent > 90:
                print(ALERT + "\n⚠️ METRIC ALERT: CORE SYSTEM IS OPERATING NEAR MAXIMUM CAPACITIES!")
            else:
                print(Fore.GREEN + Style.BRIGHT + "\n🟢 ALL SYSTEM INFRASTRUCTURE CHILLING IN SAFE PARAMETERS")
                
            print(HEADER + "\n==================================================")
            print(Fore.WHITE + "Press Ctrl+C to terminate automated scanning cycle.")
            
            # Wait 2 seconds before scraping again
            time.sleep(2)
            
    except KeyboardInterrupt:
        print(Fore.GREEN + "\n[⚡] Telemetry daemon shut down cleanly. Peace out! 🤪")

if __name__ == "__main__":
    run_dashboard()
