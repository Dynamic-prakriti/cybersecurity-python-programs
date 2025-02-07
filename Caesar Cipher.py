def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift  
    for char in text:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    return result

# User Input
text = input("Enter text: ")
shift = int(input("Enter shift value (e.g., 3): "))
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

# Processing
if mode in ["encrypt", "decrypt"]:
    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")
else:
    print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")



'''
The Caesar Cipher shifts each letter in a text by a user-defined number 
for encryption and decryption.

 Algorithm Steps:

Loop through each character in the text.
If the character is a letter, shift it by the user-specified value.
Convert the shifted letter back to its ASCII value using ord() and chr().
If decrypting, reverse the shift.
Keep spaces and special characters unchanged.
Return the encrypted or decrypted text.

'''