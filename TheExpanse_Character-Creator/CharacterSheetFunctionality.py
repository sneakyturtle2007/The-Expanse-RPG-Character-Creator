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
