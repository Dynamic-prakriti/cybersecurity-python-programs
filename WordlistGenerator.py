# Wordlist Generator
wordlist = [
    "admin",
    "password",
    "123456",
    "letmein",
    "qwerty",
    "CyberSec@2024",
    "Password",
    "supersecure123",
    "welcome",
    "password123",
    "securepass"
]

# Write wordlist to file
with open("wordlist.txt", "w") as f:
    for word in wordlist:
        f.write(word + "\n")

print("Wordlist generated: wordlist.txt")
