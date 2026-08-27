import os
from datetime import datetime

# Define the local files we are auditing and outputting
log_file_name = "server_system.log"
report_file_name = "error_report.txt"

print("⚡ Vorphix Automated Log Auditor Deploying...")

# Step 1: Create a fake sample log file for the script to analyze if it doesn't exist
if not os.path.exists(log_file_name):
    with open(log_file_name, "w") as f:
        f.write("[2026-08-26 19:45:12] INFO: System booting normally.\n")
        f.write("[2026-08-26 19:46:01] WARNING: Disk usage approaching 75% capacity.\n")
        f.write("[2026-08-26 19:47:33] CRITICAL: Database connection timeout exception!\n")
        f.write("[2026-08-26 19:48:10] INFO: Retrying network handshake protocols.\n")
        f.write("[2026-08-26 19:49:02] CRITICAL: AWS S3 Bucket access denied authentication error!\n")

# Step 2: Scan the system log file for critical issues
error_count = 0
found_alerts = []

print(f"🔍 Analyzing raw text logs inside '{log_file_name}'...")
with open(log_file_name, "r") as log:
    for line in log:
        if "CRITICAL" in line or "WARNING" in line:
            error_count += 1
            found_alerts.append(line.strip())

# Step 3: Compile and write the formal audit report
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(report_file_name, "w") as report:
    report.write(f"=== AUTOMATED INFRASTRUCTURE AUDIT REPORT ===\n")
    report.write(f"Timestamp: {now}\n")
    report.write(f"Total Security/System Exceptions Flagged: {error_count}\n")
    report.write(f"============================================\n\n")
    for alert in found_alerts:
        report.write(f"⚠️ FLAG: {alert}\n")

print(f"✨ Audit completely processed! Flagged {error_count} core issues.")
print(f"📝 Summary ledger exported to target file: '{report_file_name}'")
