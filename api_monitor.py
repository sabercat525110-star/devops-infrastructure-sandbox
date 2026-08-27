import time
import urllib.request
from datetime import datetime

# The list of server endpoints you want to check automatically
endpoints = {
    "Vorphix GitHub": "https://github.com",
    "Anaheim SDA Site": "https://anaheimsda.org",
    "Google Core Server": "https://google.com"
}

print("⚡ Vorphix Infrastructure Endpoint Monitor Booting Up...")
print("Press Ctrl+C to stop the monitoring cycle.\n")

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"--- [Scan Cycle Initiated at {now}] ---")
    
    for name, url in endpoints.items():
        try:
            # Ping the website to see if it responds
            response = urllib.request.urlopen(url, timeout=5)
            status_code = response.getcode()
            
            if status_code == 200:
                print(f"🟢 {name}: ONLINE (Status 200 OK)")
            else:
                print(f"🟡 {name}: ALERT (Status {status_code})")
                
        except Exception as e:
            # If the site is down or network cuts out, trap the exception
            print(f"🔴 {name}: CRASHED // Link Unreachable")
            print(f"⚠️ Error Logged: {e}")
            
            # Auto-generate a local crash report file
            with open("network_errors.log", "a") as log_file:
                log_file.write(f"[{now}] CRASH DETECTED on {name} ({url}). Error: {e}\n")
                
    print("\n🛌 Sleeping for 60 seconds before next automated ping check...\n")
    time.sleep(60)
