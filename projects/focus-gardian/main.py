import time
from datetime import datetime

# Hosts file location (Windows or Linux)
hosts_path = "/etc/hosts"  # For Linux/Mac
redirect = "127.0.0.1"
sites_file = "blocked_sites.txt"

# Define working hours (24-hour format)
focus_start = 9   # 9 AM
focus_end = 17    # 5 PM

def load_sites():
    """Read websites to block from blocked_sites.txt"""
    try:
        with open(sites_file, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("⚠️ blocked_sites.txt not found! Creating a new one...")
        open(sites_file, "w").close()
        return []

def block_sites(sites):
    """Block distracting sites during focus hours"""
    with open(hosts_path, "r+") as file:
        content = file.read()
        for site in sites:
            if site not in content:
                file.write(f"{redirect} {site}\n")
                print(f"🚫 Blocked: {site}")

def unblock_sites(sites):
    """Unblock sites after focus hours"""
    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in sites):
                file.write(line)
        file.truncate()
    print("✅ All sites unblocked for free browsing.")

def main():
    sites = load_sites()
    if not sites:
        print("⚠️ No sites to block! Add some in blocked_sites.txt and restart.")
        return

    print("🕒 Focus Guardian is running... Press Ctrl+C to stop.")
    while True:
        now = datetime.now()
        current_hour = now.hour

        if focus_start <= current_hour < focus_end:
            print(f"⏰ Working hours ({focus_start}:00 - {focus_end}:00) → Blocking distractions.")
            block_sites(sites)
        else:
            print(f"🌙 Non-working hours → Unblocking sites.")
            unblock_sites(sites)
        time.sleep(60 * 5)  # Check every 5 minutes

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Focus Guardian stopped by user.")
