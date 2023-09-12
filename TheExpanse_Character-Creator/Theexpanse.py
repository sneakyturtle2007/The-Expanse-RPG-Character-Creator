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
#WINDOW AND CANVAS
window = Tk()
window.geometry("500x500")
window.resizable(False,False)
window.title("Character Creator by: Luis Alejandro Blake")
canvas = Canvas( window ,bg = "#212121" , height="500", width="500")
canvas.pack()

#PROGRAM VARIABLES
currently_making_character = False
if_origin_already_set = False
background_set = False
socialClass_set = False
window_elements = []
secondary_buttons_andor_elements = []
Existing_characters = []
current_character_cards = []
current_characeter_image_path = ""
current_character_being_made = []
stat_locations = [(60,70),(65,103),(93,137),(92,165),
                      (260,280),(260,327),(260,373),(260,421),(260,467),(260,514),(260,561),(260,608),(260,655),
                      (310,40)]

displaying_character_background_constant = (Image.open("images\\Character_Sheet_1.jpg").width, Image.open("images\\Character_Sheet_1.jpg").height)
accuracy = StringVar(window)
communication = StringVar(window)
constitution = StringVar(window)
dexterity = StringVar(window)
fighting= StringVar(window)
intelligence = StringVar(window)
perception = StringVar(window)
strength = StringVar(window)
willpower = StringVar(window)
accuracy.set("")
communication.set("")
constitution.set("")
dexterity.set("")   
fighting.set("")    
intelligence.set("")
perception.set("")
strength.set("")
willpower.set("")

#CLASSES

class character:
    def __init__(self,name,age,height,weight,personality,accuracy, communication,constitution,dexterity,fighting,intelligence,perception,strength,willpower,origin,social_class,background):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.personality = personality
        self.accuracy = self.set_ability_score(accuracy)
        self.constitution = self.set_ability_score(constitution)
        self.fighting = self.set_ability_score(fighting)
        self.communication = self.set_ability_score(communication)
        self.dexterity = self.set_ability_score(dexterity)
        self.intelligence = self.set_ability_score(intelligence)
        self.perception = self.set_ability_score(perception)
        self.strength = self.set_ability_score(strength)
        self.willpower = self.set_ability_score(willpower)
        self.origin = self.set_origin(origin)
        self.social_class = self.set_social_class(social_class)
        self.background = self.set_background(background)
    
    def set_ability_score(self,ability_score):
        self.ability_score_table = [[[3],-2], [[4,5],-1],[[6,7,8],0],[[9,10,11],1], [[12,13,14],2], [[15,16,17],3], [[18],4]]
        for range_and_score in self.ability_score_table:
            if(ability_score in range_and_score[0]):
                return range_and_score[1]
    
    def set_origin(self,origin_roll):
        self.origin_roll_table = [[[1,2],["Belter"]]
                                ,[[3,4],["Earther"]]
                                ,[[5,6],["Martian"]]]
        for origin_range in self.origin_roll_table:
            if(origin_roll in origin_range[0]):
                print(origin_range[1][0])
                string = str(origin_range[1][0])
                return string
            
    def set_social_class(self,social_class):
        if(self.origin[0] == "Belter"):
            self.social_class_roll_table = [[[2,3,4,5],"Outsider"],[[6,7,8],"Lower Class"],[[9,10,11],"Middle Class"],[[12],"Upper Class"]]
            for social_class_score in self.social_class_roll_table:
                if( social_class in social_class_score[0]):
                    return social_class_score[1]
        elif(self.origin[0] == "Earther"):
            self.social_class_roll_table = [[[2,3],"Outsider"],[[4,5,6],"Lower Class"],[[7,8,9,10],"Middle Class"],[[11,12],"Upper Class"]]
            for social_class_score in self.social_class_roll_table:
                if( social_class in social_class_score[0]):
                    return social_class_score[1]
        else:
            self.social_class_roll_table = [[[2],"Outsider"],[[3,4,5,6],"Lower Class"],[[7,8,9,10,11],"Middle Class"],[[12],"Upper Class"]]
            for social_class_score in self.social_class_roll_table:
                if( social_class in social_class_score[0]):
                    return social_class_score[1]
    
    def set_background(self,backgroundroll):
        if(self.social_class == "Outsider"):
            self.background_roll_table = [[[1,2],["Bohemian"]],[[3,4],["Exile"]],[[5,6],["Outcast"]]]
            for background_score in self.background_roll_table:
                if( backgroundroll in background_score[0]):
                    return background_score[1][0]
        elif(self.social_class == "Lower Class"):
            self.background_roll_table = [[[1,2],["Military"]],[[3,4],["Laborer"]],[[5,6],["Urban"]]]
            for background_score in self.background_roll_table:
                if( backgroundroll in background_score[0]):
                    return background_score[1][0]
        elif(self.social_class == "Middle Class"):
            self.background_roll_table = [[[1,2],["Academic"]],[[3,4],["Suburban"]],[[5,6],["Trade"]]]
            for background_score in self.background_roll_table:
                if( backgroundroll in background_score[0]):
                    return background_score[1][0]
        else:
            self.background_roll_table = [[[1,2],["Aristocratic"]],[[3,4],["Corporate"]],[[5,6],["Cosmopolitan"]]]
            for background_score in self.background_roll_table:
                if( backgroundroll in background_score[0]):
                    return background_score[1][0]
        
    def __repr__(self):#  
        return self.name+ "," + self.age+ "," +self.height + "," +self.weight + "," +self.personality + "," +  str(self.accuracy) + "," + str(self.communication) + "," + str(self.constitution) + "," + str(self.dexterity) + "," + str(self.fighting) + "," + str(self.intelligence) + "," + str(self.perception) + "," + str(self.strength) + "," +str(self.willpower) + "," + str(self.origin) + "," + self.social_class + "," + self.background


#FUNCTIONS

#FUNCTIONS FOR GETTING AND DISPLAYING CHARACTER INFORMATION

def get_characters():
    global current_character_cards,Existing_characters
    characters = []
    index = 0
    for image in os.listdir("images\\"):
        if(str(image) != "noimage.jpg" and str(image) != "photo1.jpg" and str(image) != "Belter.jpg" and str(image) != "TheExpanse-Earther.jpg" and str(image) != "Martian.jpg" and str(image) != "Character_Sheet_1.jpg" and str(image) != "Character_Sheet_2.jpg"):
            current_character = []
            current_character.append(str(image))
            with open("Characters.txt") as characters_text:
                characters2 = characters_text.readlines()
                
                Character = characters2[index].split(",")
                
                Existing_characters.append(character(Character[0],Character[1],Character[2],Character[3],Character[4],int(Character[5]),int(Character[6]),int(Character[7]),int(Character[8]),int(Character[9]),int(Character[10]),int(Character[11]),int(Character[12]),int(Character[13]),int(Character[14]),int(Character[15]),int(Character[16])))
                print(Character)
                current_character.append(Character[0])
            characters.append(current_character)
            
            index += 1
    current_character_cards = characters
    return characters


def create_character_card(image_path,x,y, parameters,name):
    global window_elements
    img = Image.open(image_path)
    resized_image = img.resize((90, 80), Image.NEAREST)
    image = ImageTk.PhotoImage(resized_image)

    card_id = canvas.create_image(x, y, image=image, anchor=tk.NW)
    
    canvas.tag_bind(card_id, "<Button-1>", lambda card_item=(card_id, image, parameters) : display_character_ClickedOn("False",parameters))#event,
    character_name_label = tk.Label(window, text = name, bg="#212121", fg = "#E6E6E6",font=("Arial", 10))
    character_name_label.pack()
    character_name_label.place(x= x+(35-(len(name)*3)), y = y+80)
    window_elements.append(character_name_label)

    
def display_characters(characters):
    global window_elements,secondary_buttons_andor_elements,Existing_characters
    
    for element in window_elements:
        element.destroy()
    for element in secondary_buttons_andor_elements:
        element.destroy()
    window_elements = []
    canvas.config(width=500,height=500)
    window.geometry("500x500")
    index = 0
    increment = 40
    
    for character in characters:
        create_character_card("images\\" + character[0], 37 + (110 *index), increment,Existing_characters[index], character[1])
        if(index % 3 == 0 and index != 0):
            index -= index
            increment += 120
        else:
            index += 1
    Add_characer_button = Button(window, bg="#424242", fg = "#E6E6E6",text="Add Character",font=("Arial", 10),command=lambda:display_charactermaker())           
    Add_characer_button.pack()
    Add_characer_button.place(x=380,y=440)
    window_elements.append(Add_characer_button)    
        
        
def display_character_ClickedOn(ifbackpage,stats):
    global window_elements,displaying_character_background_constant,secondary_buttons_andor_elements
    
    window.geometry("+%d+%d" %(window.winfo_x(),0))
    if ifbackpage == "True":
        print("helloo does this functon work")
        for elements in window_elements:
            elements.destroy()
        for element in secondary_buttons_andor_elements:
            elements.destroy()
        window_elements = []
        character_sheet = Image.open("images\\Character_Sheet_2.jpg")
        character_sheet_resized = character_sheet.resize((displaying_character_background_constant[0]+30, displaying_character_background_constant[1]-10), Image.NEAREST)
        character_sheet_background = ImageTk.PhotoImage(character_sheet_resized)
        geometry_text = str(displaying_character_background_constant[0]-10) + "x" + str(displaying_character_background_constant[1]-30)
        window.geometry(geometry_text)
        canvas.config(width=displaying_character_background_constant[0],height=displaying_character_background_constant[1])
        background = tk.Label(window,image=character_sheet_background)
        background.image = character_sheet_background
        background.pack()
        background.place(x=-20,y=0)
        
        window_elements.append(background)
        #display_stats(stats)
        back_button, edit_button  = Button(window, bg="#424242", fg = "#E6E6E6",text="Back",font=("Arial", 10),command=lambda:display_character_ClickedOn(False,stats)), Button(window, bg="#424242", fg = "#E6E6E6",text="Edit",font=("Arial", 10),command=lambda:Edit_displayed_character(stats))
    
        back_button.pack()
        edit_button.pack()
        back_button.place(x=10,y=10)
        
        
        window_elements.append(back_button)
    else: 
        for element in window_elements:
            element.destroy()
        canvas.delete("all")
        window_elements = []
        character_sheet = Image.open("images\\Character_Sheet_1.jpg")
        character_sheet_resized = character_sheet.resize((character_sheet.width+10, character_sheet.height-10), Image.NEAREST)
        character_sheet_background = ImageTk.PhotoImage(character_sheet_resized)
        geometry_text = str(character_sheet.width-10) + "x" + str(character_sheet.height-30)
        window.geometry(geometry_text)
        canvas.config(width=character_sheet.width,height=character_sheet.height)
        background = tk.Label(window,image=character_sheet_background)
        background.image = character_sheet_background
        background.pack()
        background.place(x=-20,y=0)
        window_elements.append(background)
        display_stats(stats)
        back_button, edit_button, next_button  = Button(window, bg="#424242", fg = "#E6E6E6",text="Back",font=("Arial", 10),command=lambda:display_characters(current_character_cards)), Button(window, bg="#424242", fg = "#E6E6E6",text="Edit",font=("Arial", 10),command=lambda:Edit_displayed_character(stats)), Button(window, bg="#424242", fg = "#E6E6E6",text="Next",font=("Arial", 10),command=lambda:display_character_ClickedOn("True",stats))
        
        next_button.pack()
        back_button.pack()
        edit_button.pack()
        
        back_button.place(x=10,y=10)
        next_button.place(x=500,y=600)
        
        window_elements.append(next_button) 
        window_elements.append(back_button)
        
        
def display_stats(stats):
    global secondary_buttons_andor_elements,stat_locations
    print(stats)
    
    stat_values = [stats.name,stats.origin,stats.background,stats.social_class,stats.accuracy,stats.communication,stats.constitution,stats.dexterity,stats.fighting,stats.intelligence,stats.perception,stats.strength,stats.willpower,stats.age]#,stats.height,stats.weight,stats.personality
    index = 0
    for values in stat_values:
        if index < 4:
            stat_label = tk.Label(window, text = values, bg="#FFFFFF", fg = "#000000",font=("Arial", 10))
        elif index < 13:
            stat_label = tk.Label(window, text = values, bg="#FFFFFF", fg = "#000000",font=("Arial", 14))
        else:
            stat_label = tk.Label(window, text =   values, bg="#FFFFFF", fg = "#000000",font=("Arial", 9))
        stat_label.pack()
        stat_label.place(x= stat_locations[index][0], y = stat_locations[index][1])
        secondary_buttons_andor_elements.append(stat_label)
        index += 1
    

def Edit_displayed_character(stats):
    global secondary_buttons_andor_elements
    print("temp")
    for element in secondary_buttons_andor_elements:
        element.destroy()
    secondary_buttons_andor_elements = []
    
    
    
#FUNCTIONS FOR CHARACTER CREATION

def display_charactermaker():
    global window_elements,current_character_cards,current_character_being_made,currently_making_character,current_characeter_image_path
    currently_making_character = True
    
    for element in window_elements:
        element.destroy()
    canvas.delete("all")
    window_elements = []
    current_characeter_image_path = "images\\noimage.jpg"
    img = Image.open("images\\noimage.jpg")
    resized_image = img.resize((170, 200), Image.NEAREST)
    image = ImageTk.PhotoImage(resized_image)
    
    character_image = Button(window, bg="#424242",image = image,compound="bottom",
                                font=("Arial", 10),command=choose_image)
    character_image.image = image
    character_image.pack()
    character_image.place(x=165,y=20)
    window_elements.append(character_image)
    
    name_label = tk.Label(window, text = "Name", bg="#212121", fg = "#E6E6E6",font=("Arial", 10))
    name_label.pack()
    name_label.place(x=232,y=230)
    window_elements.append(name_label)
    
    name = tk.Text(window, height=1,width=15)
    name.pack()
    name.place(x=192,y=260)
    window_elements.append(name)
    
    height_label = tk.Label(window, text = "Height (in)", bg="#212121", fg = "#E6E6E6",font=("Arial", 10))
    height_label.pack()
    height_label.place(x=159,y=285)
    window_elements.append(height_label)
    
    height = tk.Text(window, height=1,width=7)
    height.pack()
    height.place(x=162,y=310)
    window_elements.append(height)
    
    weight_label = tk.Label(window, text = "Weight (lbs)", bg="#212121", fg = "#E6E6E6",font=("Arial", 10))
    weight_label.pack()
    weight_label.place(x=289,y=285)
    window_elements.append(weight_label)
    
    weight = tk.Text(window, height=1,width=7)
    weight.pack()
    weight.place(x=292,y=310)
    window_elements.append(weight)
    
    age_label = tk.Label(window, text = "Age", bg="#212121", fg = "#E6E6E6",font=("Arial", 10))
    age_label.pack()
    age_label.place(x=240,y=285)
    window_elements.append(age_label)
    
    age = tk.Text(window,height=1, width=5)
    age.pack()
    age.place(x=235,y=310)
    window_elements.append(age)
    
    personality_label = tk.Label(window, text = "Personality", bg="#212121", fg = "#E6E6E6",font=("Arial", 10))
    personality_label.pack()
    personality_label.place(x=215,y=335)
    window_elements.append(personality_label)
    
    personality = tk.Text(window, wrap="word",height=7, width=40)
    personality.pack()
    personality.place(x=90,y=360)
    window_elements.append(personality)
    
    back_button = Button(window, bg="#424242", fg = "#E6E6E6",text="Back",font=("Arial", 10),command=lambda:display_characters(current_character_cards))           
    back_button.pack()
    back_button.place(x=20,y=20)
    window_elements.append(back_button)
    
    next_button = Button(window, bg="#424242", fg = "#E6E6E6",text="Next",font=("Arial", 10),command=lambda:stat_setter())
    next_button.pack()
    next_button.place(x=450,y=450)
    window_elements.append(next_button)
    if (len(current_character_being_made) > 0):
        index = 0
        for element in window_elements:
            if isinstance(element,Text):
                element.insert("end-1c", current_character_being_made[index])
                index += 1
        print("done")
        
        
def stat_setter():
    global accuracy, communication, constitution, dexterity, fighting, intelligence, perception, strength,willpower, window_elements,current_character_being_made,currently_making_character,current_characeter_image_path
    
    stats, stats_text, current_character_being_made, ifanyinformationempty = [accuracy, communication, constitution, dexterity, fighting,intelligence, perception, strength, willpower], ["Accuracy", "Comm.", "Constitution", "Dexterity", "Fighting","Intelligence", "Perception", "Strength", "Willpower"], [], False

    window.geometry("500x500")
    canvas.config(width=500,height=500)

    for index in window_elements:
        if isinstance(index,Text):
            if index.get("1.0", "end-1c") == "" or current_characeter_image_path == "images\\noimage.jpg":
                ifanyinformationempty = True
                
    if ifanyinformationempty != True:
        if(currently_making_character):
            for index in window_elements:
                if isinstance(index,Text):
                    current_character_being_made.append(index.get("1.0", "end-1c"))  # Use the new function
                    print(current_character_being_made)
                
        for element in window_elements:
                element.destroy()
                
        window_elements = []
        canvas.delete("all")
        
        location = 0
        increment= 70
        for index in range(0,9): 
            stat_label, dropdownmenu = tk.Label(window, text = stats_text[index], bg="#212121", fg = "#E6E6E6",font=("Arial", 10)), OptionMenu(window, stats[index], "3", "4", "5", "6", "7", "8", "9", "10", "11", "12","13","14","15","16","17","18")
            
            stat_label.pack()
            dropdownmenu.pack()
            
            stat_label.place(x= 37 + (90 *location), y = increment-20)
            dropdownmenu.place(x = (37 + (90 *location)), y = increment)
            
            window_elements.append(stat_label)
            window_elements.append(dropdownmenu)

            location += 1
            if index != 0 and index % 4 == 0  :
                location -= location
                increment += 120
                
        back_button, done_button  = Button(window, bg="#424242", fg = "#E6E6E6",text="Back",font=("Arial", 10),command=lambda:display_charactermaker()), Button(window, bg="#424242", fg = "#E6E6E6",text="Done",font=("Arial", 10),command=lambda:origin_setter())
        
        back_button.pack()
        done_button.pack()
        
        back_button.place(x=20,y=20)   
        done_button.place(x=450,y=450)
        
        window_elements.append(back_button)
        window_elements.append(done_button)
   
   
def origin_setter():
    global accuracy, communication,constitution, dexterity, fighting, intelligence, perception, strength, willpower,window_elements,window,canvas
    stats = [accuracy, communication, constitution, dexterity, fighting,intelligence, perception, strength, willpower]
    ifanystatsareempty = False 
    
    for index in stats:
        if index.get() == "":
            ifanystatsareempty = True
    if ifanystatsareempty != True:
        window.geometry("1500x700")
        canvas.config(width=2000,height=1000)
        for stat in stats:
            current_character_being_made.append(stat.get())
        print(current_character_being_made)
        origin_images = ["Belter.jpg","TheExpanse-Earther.jpg","Martian.jpg"]
        origin_text = ["Belter\n\nYou were born and raised in the black, on the station or ship,\nand have lived most, if not all, of your life out in the\nBelt or beyond.Separated from death by nothing more than\nbasic support systems your whole life, you have learned to be\ncautious and aware of your environment. As a Belter, your\ncharacter has the following traits:\n\n- Your native gravity is microgravity. Belters are most comfortable\n'on the float' and handle moving in free-fall easily. You automatically\nhave the Dexterity (Free-fall) focus. Conversly, Earth-normal\ngravity is crushingly heavy for a Belter.\n\n- You speak Belter Creole, a combination of loan-words and phrases\nfrom various languages, combined with gestures useful for communicating\nwhile wearing vac suit and unable to speak.\n\n- Belters tend to be tall and willowy as a result of being raised\nin low or microgravityenvironments. Regimens of bone-density\ndrugs and genetic treatments are needed to keep Belters healthy,\nand some Belters have minor physical abnormatlities\nBecause of this.\n\n- Belters often have a diverse ethnic heritage, given\nthe 'melting pot' of the Belt, with ancestors from any\ndifferent Earth cultures.",
                       "Earther\n\nWith a population  of some 30 billion, many Earthers are unemplayed\n and live on government-provided Basic Assitance (generally\nknown as just 'Basic') which provides for their essential\nfood, housing, and medical needs, but little else. You are\nlikely one of the few to leave earth to find a new\nlife elsewhere. As an Earther, your character has the following\ntraits:\n\n- Your native gravity is normal gravity-'Earth-normal' or 1g.\nEarthers can and do learn to operate in lower gravity,\nbut lack the instincts of people raised in it.\n\n- Earthers have greater muscle and bone density from being\nraised in a gravity well, making them shorter and\n more broadly build than Belters or even nativ-born Martians, but\nEarthers in space need regular exercise and medical treatments to\navoid muscle atrophy and bone density loss.",
                       "Martian\n\nBorn in the Martian Congressional Republic, your life has been\ninfluenced by the Martian dream: to terraform the RedPlanet\ninto a lush and life-sustaining garden. Like the generations\nbefore you, you know that you will likely never see the completion\nof this work in your lifetime. As a Martian, your\ncharacter has the following traits:\n\n- Your native gravity is low, the gravity of Mars rather\nthan Earth. Martians are more comfortable with microgravity\nthan Earthers, and better able to tolerate a full 1g than Belters,\noperating in-between."]
        for element in window_elements:
            element.destroy()
        window_elements = []
        
        height = 40
        Belter_img, Earther_img, Martian_img = Image.open("images\\Belter.jpg"), Image.open("images\\TheExpanse-Earther.jpg"),  Image.open("images\\Martian.jpg")
        
        Belter_resized, Earther_resized, Martian_resized = Belter_img.resize((250, 180), Image.NEAREST), Earther_img.resize((250, 180), Image.NEAREST),  Martian_img.resize((250,180),Image.NEAREST) 
        
        Belter_PhotoImage, Earther_PhotoImage, Martian_PhotoImage = ImageTk.PhotoImage(Belter_resized), ImageTk.PhotoImage(Earther_resized), ImageTk.PhotoImage(Martian_resized)
        
        Belter_Button_text, Earther_Button_text, Martian_Button_text  = origin_text[0], origin_text[1], origin_text[2]
        
        Belter_Button, Earther_Button, Martian_Button = Button(window, bg="#424242", fg = "#E6E6E6",text=Belter_Button_text ,image = Belter_PhotoImage,compound="bottom",
                                    font=("Arial", 10),command= lambda: origin_stat_setter("Belter")), Button(window,bg="#424242", fg = "#E6E6E6",text=Earther_Button_text ,image = Earther_PhotoImage,compound="bottom",
                                    font=("Arial", 10),command= lambda: origin_stat_setter("Earther")),  Button(window,bg="#424242", fg = "#E6E6E6",text=Martian_Button_text ,image = Martian_PhotoImage,compound="bottom",
                                    font=("Arial", 10),command= lambda: origin_stat_setter("Martian"))
        
        Belter_Button.image, Earther_Button.image,  Martian_Button.image  = Belter_PhotoImage, Earther_PhotoImage, Martian_PhotoImage
        
        Belter_Button.pack()
        Earther_Button.pack()
        Martian_Button.pack()
        
        window_elements.append(Belter_Button)
        window_elements.append(Earther_Button)
        window_elements.append(Martian_Button)
        
        Belter_Button.place(x = 60 + (500 * 0), y = height)
        Earther_Button.place(x = 60 + (500 * 1),y = height)
        Martian_Button.place(x = 60 + (500 * 2),y = height)
        
        back_button = Button(window, bg="#424242", fg = "#E6E6E6",text="Back",font=("Arial", 10),command=lambda:stat_setter())
        back_button.pack()
        back_button.place(x=20,y=10)    
        window_elements.append(back_button)
    
    
def origin_stat_setter(image_name):
    global origin_setter
    if(origin_setter):
        print(image_name)
        if(image_name == "Belter"):
            current_character_being_made.append("1")
        elif(image_name == "Earther"):
            current_character_being_made.append("3")
        elif(image_name == "Martian"):
            current_character_being_made.append("5")
        print(current_character_being_made)
        origin_setter = True
    else: 
        if(image_name == "Belter"):
            current_character_being_made[14] = "1"
        elif(image_name == "Earther"):
            current_character_being_made[14] = "3"
        elif(image_name == "Martian"):
            current_character_being_made[14] = "5"
        print(current_character_being_made)
    social_class_setter_and_Background_setter()
    

def social_class_setter_and_Background_setter():
    global window_elements
    for elements in window_elements:
        elements.destroy()
    window.geometry("500x500")
    window_elements = []
    increment= 70
    
    Outsider_Button, LowerClass_Button, MiddleClass_Button, UpperClass_Button= Button(window, text = "Outsider", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_background_options("Outsider")), Button(window, text= "Lower Class", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_background_options("Lower Class")), Button(window, text = "Middle Class", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_background_options("Middle Class")),  Button(window, text = "Upper Class", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_background_options("Upper Class"))
    
    Outsider_Button.pack()
    LowerClass_Button.pack()
    MiddleClass_Button.pack()   
    UpperClass_Button.pack()
    
    Outsider_Button.place(x= 37 + (110 *0), y = increment)
    LowerClass_Button.place(x= 37 + (110 *1), y = increment)
    MiddleClass_Button.place(x= 37 + (110 *2), y = increment)
    UpperClass_Button.place(x= 37 + (110 *3), y = increment)
    
    window_elements.append(Outsider_Button)
    window_elements.append(LowerClass_Button)
    window_elements.append(MiddleClass_Button)  
    window_elements.append(UpperClass_Button)
    
    back_button = Button(window, bg="#424242", fg = "#E6E6E6",text="Back",font=("Arial", 10),command=lambda:origin_setter())
    back_button.pack()
    back_button.place(x=20,y=10)
    window_elements.append(back_button)

        
def display_background_options(text):
    global secondary_buttons_andor_elements,socialClass_set,current_character_being_made
    for elements in secondary_buttons_andor_elements:
        elements.destroy()
    secondary_buttons_andor_elements = []
    if(text== "Outsider"):
        Bohemian_Button, Exile_Button, Outcast_Button = Button(window, text = "Bohemian", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(1)), Button(window, text = "Exile", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(3)), Button(window,text= "Outcast", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(5))
        
        Bohemian_Button.pack()
        Exile_Button.pack() 
        Outcast_Button.pack()
        
        Bohemian_Button.place(x= 37 + (110 *0), y = 120)
        Exile_Button.place(x= 37 + (110 *1), y = 120)
        Outcast_Button.place(x= 37 + (110 *2), y = 120)
        
        secondary_buttons_andor_elements.append(Bohemian_Button)
        secondary_buttons_andor_elements.append(Exile_Button)
        secondary_buttons_andor_elements.append(Outcast_Button)
        if(socialClass_set):
            current_character_being_made[15] = "2"
        else:
            current_character_being_made.append("2")
            socialClass_set = True
        
    elif(text == "Lower Class"):
        Military_Button, Laborer_Button, Urban_Button = Button(window, text= "Military", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(1)), Button(window, text = "Laborer", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(3)), Button(window, text = "Urban", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(5))
        
        Military_Button.pack()
        Laborer_Button.pack()
        Urban_Button.pack()
        
        Military_Button.place(x= 37 + (110 *0), y = 120)
        Laborer_Button.place(x= 37 + (110 *1), y = 120)
        Urban_Button.place(x= 37 + (110 *2), y = 120)
        
        secondary_buttons_andor_elements.append(Military_Button)
        secondary_buttons_andor_elements.append(Laborer_Button)
        secondary_buttons_andor_elements.append(Urban_Button)
        
        if(socialClass_set):
            current_character_being_made[15] = "6"
        else:
            current_character_being_made.append("6")
            socialClass_set = True
    elif(text == "Middle Class"):
        Academic_Button, Suburban_Button, Trade_Button  = Button(window, text = "Academic", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(1)), Button(window, text = "Suburban", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(3)), Button(window, text = "Trade", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(5))
        
        Academic_Button.pack()
        Suburban_Button.pack()
        Trade_Button.pack()
        
        Academic_Button.place(x= 37 + (110 *0), y = 120)
        Suburban_Button.place(x= 37 + (110 *1), y = 120)
        Trade_Button.place(x= 37 + (110 *2), y = 120)
        
        secondary_buttons_andor_elements.append(Academic_Button)
        secondary_buttons_andor_elements.append(Suburban_Button)
        secondary_buttons_andor_elements.append(Trade_Button)
        if(socialClass_set):
            current_character_being_made[15] = "9"
        else:
            current_character_being_made.append("9")
            socialClass_set = True
    elif(text == "Upper Class"):
        Aristocratic_Button, Corporate_Button, Cosmopolitan_Button  = Button(window, text = "Aristocratic", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(1)), Button(window, text = "Corporate", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(3)), Button(window, text = "Cosmopolitan", bg="#212121", fg = "#E6E6E6",font=("Arial", 11),command=lambda:display_Save_Character_Button_and_Save_Choice(5))
        
        Aristocratic_Button.pack()
        Corporate_Button.pack()
        Cosmopolitan_Button.pack()
        
        Aristocratic_Button.place(x= 37 + (110 *0), y = 120)
        Corporate_Button.place(x= 37 + (110 *1), y = 120)
        Cosmopolitan_Button.place(x= 37 + (110 *2), y = 120)

        secondary_buttons_andor_elements.append(Aristocratic_Button)
        secondary_buttons_andor_elements.append(Corporate_Button)
        secondary_buttons_andor_elements.append(Cosmopolitan_Button)
        if(socialClass_set):
            current_character_being_made[15] = "12"
        else:
            current_character_being_made.append("12")
            socialClass_set = True
    print(current_character_being_made)


def display_Save_Character_Button_and_Save_Choice(Current_Score):
    global window_elements, current_character_being_made, background_set
    print(current_character_being_made)
    Save_Character_Button = Button(window, bg="#424242", fg = "#E6E6E6",text="Save Character",font=("Arial", 10),command=lambda:save_character())
    Save_Character_Button.pack()
    Save_Character_Button.place(x=420,y=450)
    window_elements.append(Save_Character_Button)
    if(background_set):
        current_character_being_made[16] = Current_Score
    else:
        current_character_being_made.append(Current_Score)
        background_set = True
        

def choose_image():
    global current_characeter_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
    if file_path:
        current_characeter_image_path = file_path
        image = Image.open(file_path)
        resized_image = image.resize((170, 200), Image.NEAREST)
        photo = ImageTk.PhotoImage(resized_image)
        window_elements[0].config(image=photo)
        window_elements[0].image = photo

 
def save_image(image_path):
    destination_path = os.path.join("images", os.path.basename(image_path))
    shutil.copy(image_path, destination_path)


def save_character():
    current_character_to_string = ""
    old_characters_text = ""
    
    old_characters = open("Characters.txt", "r")
    
    counter = 0
    for index in current_character_being_made:
        if counter == len(current_character_being_made)-1:
            current_character_to_string += str(index)
        else:
            current_character_to_string += str(index) + ","
        counter += 1
    old_characters_text = old_characters.readlines()
    Characters = open("Characters.txt", "w")
    print(old_characters_text)
    old_characters_text += "\n"
    old_characters_text += current_character_to_string
    print(current_character_cards)
    print(current_character_cards)
    print(old_characters_text)
    Characters.writelines(old_characters_text)
    print(current_characeter_image_path)
    save_image(current_characeter_image_path)
    old_characters.close()  
    Characters.close()  
    display_characters(get_characters())    
        
    
#MAIN PROGRAM

character = get_characters()
display_characters(character)

window.mainloop()
