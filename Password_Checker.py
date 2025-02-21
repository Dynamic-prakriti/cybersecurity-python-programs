import hashlib
import requests

def check_password(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    first5, tail = sha1_hash[:5], sha1_hash[5:]

    response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")

    if tail in response.text:
        print("⚠️ This password has been found in a data breach! Choose a stronger password.")
    else:
        print("✅ This password is safe (not found in leaks).")

# User input
password = input("Enter a password to check: ")
check_password(password)




'''
This project checks if a password has been leaked using the Have I Been Pwned API.


Algorithm:
Convert the password into SHA-1 hash.
Send the first 5 characters of the hash to Have I Been Pwned API.
Check if the remaining hash part exists in the API response.
If found, alert the user that the password has been leaked.
'''