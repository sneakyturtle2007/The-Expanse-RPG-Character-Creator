#IMPORTS
import os
try:
    import shutil
except ImportError:
    import subprocess
    subprocess.call(['pip', 'install', 'shutil'])
    import shutil
try:
    import tkinter as tk
    import ttkbootstrap as ttk
 
    from tkinter import *
    from tkinter import filedialog
except ImportError:
    import subprocess
    subprocess.call(['pip', 'install', 'tkinter'])
    subprocess.call(['pip', 'install', 'ttkbootstrap'])
    import tkinter as tk
    import ttkbootstrap as ttk
  
    from tkinter import *
    from tkinter import filedialog
try:
    from PIL import Image, ImageTk
except ImportError:
    import subprocess
    subprocess.call(['pip', 'install', 'Pillow'])
    from PIL import Image
try:
    import lorem
except ImportError:
    import subprocess
    subprocess.call(['pip', 'install', 'lorem'])
    import lorem


# Window 
window = ttk.Window(themename = 'darkly')
window.geometry("500x500")
window.resizable(False,False)
window.title("The Expanse Character Creator By: Luis Blake")
# Title
title = ttk.Label(master = window, text = "The Expanse Character Creator By: Luis Blake", font = ("Times New Roman", 14, "bold"))

title.pack()
def convert():
    output.config(text = entry.get())
# Input field

input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame, width = 50)
entry.pack(side = "left")
enter = ttk.Button(master = input_frame, text = "Enter",command=convert)
enter.pack(side = "right")
input_frame.pack()    

output = ttk.Label(master = window, text = "Output")
output.pack()
window.mainloop()