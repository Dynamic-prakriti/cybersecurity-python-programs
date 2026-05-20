import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

# User Input
password = input("Enter password to hash: ")
hashed_password = hash_password(password)

print(f"Hashed Password: {hashed_password.decode()}")

# Verify
check = input("Re-enter password to verify: ")
if verify_password(check, hashed_password):
    print("Password match!")
else:
    print("Password does not match.")
