import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User Input
password = input("Enter password to hash: ")
hashed_password = hash_password(password)

print(f"Hashed Password: {hashed_password}")


'''
Hashes a password using SHA-256 
to securely store and compare passwords.

Algorithm Steps:

Take user input (password).
Convert the password into bytes using .encode().
Apply SHA-256 hashing using hashlib.sha256().
Convert the hashed value into a readable hex format using .hexdigest().
Display the hashed password.
'''
