import re
from email.parser import Parser

def extract_domain(address):
     # Extracts the domain part from an email address (e.g., @gmail.com)
    match = re.search(r'@([\w\.-]+)', address)
    return match.group(1).lower() if match else None

def analyze_headers(headers_text, index, trusted_domains):
    headers = Parser().parsestr(headers_text)    # Parse raw header block into a dictionary

    from_address = headers.get("From", "")
    reply_to = headers.get("Reply-To", "")
    return_path = headers.get("Return-Path", "")

    from_domain = extract_domain(from_address)
    reply_to_domain = extract_domain(reply_to)
    return_path_domain = extract_domain(return_path)

    print(f"\n Email #{index + 1}")
    print(f"From: {from_address}")
    print(f"Reply-To: {reply_to}")
    print(f"Return-Path: {return_path}")

    flags = []
    if from_domain not in trusted_domains:
        flags.append("⚠️ From domain not in trusted list")

    if reply_to_domain and reply_to_domain != from_domain:
        flags.append("⚠️ Reply-To domain differs from From")

    if return_path_domain and return_path_domain != from_domain:
        flags.append("⚠️ Return-Path differs from From")

    if flags:
        print("!!! Potential Spoofing Detected:")
        for flag in flags:
            print(" -", flag)
    else:
        print(" No spoofing indicators detected.")

def process_multiple_emails(file_path):
     # Read the file containing multiple headers
    with open(file_path, 'r') as f:
        content = f.read()

  
    # Split different headers using double newline as separator
    email_blocks = content.strip().split("\n\n")

    #Define trusted domain
    trusted_domains = ["gmail.com", "yourdomain.com", "outlook.com"]


    # Analyze each header block one by one
    for idx, block in enumerate(email_blocks):
        analyze_headers(block, idx, trusted_domains)

if __name__ == "__main__":
    process_multiple_emails("sample_email_header.txt")
