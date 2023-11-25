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
    from tkinter import *
    from tkinter import filedialog
except ImportError:
    import subprocess
    subprocess.call(['pip', 'install', 'tkinter'])
    import tkinter as tk
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

def diceroll():
    print("test")
    
def adding_subtracting_Fortune():
    print("temp")
    
def Visual_fortune_points(window,fortune,canvas):
    x_square = 680
    y_square = 500
    side_length = 5
    for row in range(30):
        for column in range(3):
            if(row*column <= fortune):
                x_square = 680 + (column * (side_length + 2))
                y_square = 500 - (row * (side_length+2))
                canvas.create_rectangle(x_square, y_square, x_square+side_length, y_square+side_length,fill="blue")
            else:
                canvas.create_rectangle(x_square, y_square, x_square+side_length, y_square+side_length,fill="white")
def FortunePointsInteractable(window,fortune,canvas):
    Visual_fortune_points(window,fortune,canvas)
    print("temp")
    
    
    
    
def settingUp_Interactables(window,elements,fortune,canvas):
    
    print("temp")
    return elements,fortune
    