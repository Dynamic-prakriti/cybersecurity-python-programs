import hashlib
import time

def calculate_hash(file_path):
    """Compute SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None

def monitor_files(file_list):
    """Monitor files for unauthorized changes."""
    file_hashes = {file: calculate_hash(file) for file in file_list}

    print("\nMonitoring for changes... Press Ctrl+C to stop.\n")

    try:
        while True:
            for file in file_list:
                new_hash = calculate_hash(file)
                if new_hash and new_hash != file_hashes[file]:
                    print(f"[ALERT] File changed: {file}")
                    file_hashes[file] = new_hash  # Update stored hash
            time.sleep(2)  # Add delay to prevent CPU overload
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

# User input
files_to_monitor = input("Enter files to monitor (comma-separated): ").split(",")
files_to_monitor = [file.strip() for file in files_to_monitor]

monitor_files(files_to_monitor)




# Algorithm
'''

1. Prompt user to enter file names to monitor.
2. Convert input into a list of file paths.
3. Initialize an empty dictionary `file_hashes = {}`.
4. For each file in the list:
   a. Open the file in binary mode.
   b. Compute its SHA-256 hash.
   c. Store the hash in `file_hashes[file]`.
5. Print "Monitoring for changes... Press Ctrl+C to stop."
6. Enter an infinite loop:
   a. Wait for 2 seconds.
   b. For each file in the list:
      i. Compute its new SHA-256 hash.
      ii. Compare with the stored hash.
      iii. If the hashes do not match:
          - Print "[ALERT] File changed: filename"
          - Update the stored hash with the new one.
   c. Repeat until the user manually stops the program (Ctrl+C).
7. When interrupted, print "Monitoring stopped."

'''
# files created for testing: test1.txt, test2.txt