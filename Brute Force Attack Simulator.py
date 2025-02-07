def brute_force(password_list, correct_password):
    for password in password_list:
        print(f"Trying: {password.strip()}")  # Displaying each attempt
        if password.strip() == correct_password:
            print(f"Password found: {password.strip()}")
            return True
    print("Password not found.")
    return False

# Read wordlist from file
wordlist_file = "wordlist.txt"
try:
    with open(wordlist_file, "r") as file:
        password_list = file.readlines()

    # User input: Correct password to test
    correct_password = input("Enter a password to test against wordlist: ")

    # Run brute-force attack simulation
    brute_force(password_list, correct_password)

except FileNotFoundError:
    print("Wordlist file not found! Please ensure 'wordlist.txt' exists in the same directory.")



'''
Simulates a dictionary-based 
brute-force attack on a user-provided password.

Algorithm Steps:

Read password guesses from wordlist.txt.
Take user input for the correct password.
Loop through the wordlist:
If a password matches, print "Password found".
If none match, print "Password not found".
'''