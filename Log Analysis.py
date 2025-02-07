import re

def analyze_logs(log_file):
    try:
        with open(log_file, 'r') as file:
            logs = file.readlines()
        
        suspicious_attempts = [log for log in logs if "Failed password" in log]
        
        print(f"Total Failed Login Attempts: {len(suspicious_attempts)}")
        for attempt in suspicious_attempts:
            ip = re.search(r'(\d+\.\d+\.\d+\.\d+)', attempt)
            if ip:
                print(f"Suspicious IP: {ip.group()}")

    except FileNotFoundError:
        print("Log file not found! Please provide a valid file.")

# User Input
log_file = input("Enter log file path (e.g., /var/log/auth.log or logs.txt): ")

# Run Log Analysis
analyze_logs(log_file)


'''
Analyzes a user-provided log file for failed login attempts.

 Algorithm Steps:

User provides a log file.
Read the log file line by line.
Check each line for "Failed password" (indicating a failed login attempt).
Use Regex (re.search()) to extract IP addresses.
Display the count of failed login attempts and suspicious IPs.

'''
