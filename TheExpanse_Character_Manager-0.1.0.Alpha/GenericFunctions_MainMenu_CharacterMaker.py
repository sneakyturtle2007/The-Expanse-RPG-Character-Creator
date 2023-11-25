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

from CharacterClass import character

#WINDOW AND CANVAS

def convert_to_die_roll(ability_score):
    ability_score_table = [[[3],-2], [[4,5],-1],[[6,7,8],0],[[9,10,11],1], [[12,13,14],2], [[15,16,17],3], [[18],4]]
    
    for range_and_score in ability_score_table:
        if(ability_score == range_and_score[1]):
            print("ability score : " , ability_score , "\n")
            
            print("number of that score: " , range_and_score[0][0], "\n")
            
            return range_and_score[0][0]
    print("ERROR: ability score not found\n\n\n")
   
def get_characters():
    
    characters = []
    current_character_cards = []
    Existing_characters_current = []
    index = 0
    for image in os.listdir("images\\"):
        
        if(str(image) != "noimage.jpg" and str(image) != "photo1.jpg" and str(image) != "Belter.jpg" and str(image) != "TheExpanse-Earther.jpg" and str(image) != "Martian.jpg" and str(image) != "Character_Sheet_1.jpg" and str(image) != "Character_Sheet_2.jpg"):
           
            current_character = []
            current_character.append(str(image))
            
            with open("TheExpanseCharacterCreator.txt") as characters_text:
                characters2 = characters_text.readlines()
                
                Character = characters2[index].split(",")
                
               
                temp_character = character(Character[0],Character[1],Character[2],Character[3],Character[4],convert_to_die_roll(int(Character[5])),convert_to_die_roll(int(Character[6])),convert_to_die_roll(int(Character[7])),convert_to_die_roll(int(Character[8])),convert_to_die_roll(int(Character[9])),convert_to_die_roll(int(Character[10])),convert_to_die_roll(int(Character[11])),convert_to_die_roll(int(Character[12])),convert_to_die_roll(int(Character[13])),Character[14],Character[15],Character[16],Character[17])

                Existing_characters_current.append(temp_character)
             
                current_character.append(Character[0])
            characters.append(current_character)
            
            index += 1
    current_character_cards = characters
    return characters, current_character_cards, Existing_characters_current



