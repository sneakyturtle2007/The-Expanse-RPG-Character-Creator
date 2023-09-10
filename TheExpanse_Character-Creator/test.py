import tkinter as tk
from PIL import Image, ImageTk

# Create a list to store character card images and their associated parameters
character_cards = []

# Function to handle the click event for each character card
def character_card_clicked(card_item):
    # Execute the function with the associated parameters
    print(f"Function executed with parameters: {card_item[1]}")
    move_card_down(card_item)

# Function to move the card slightly down and then return it to its original position
def move_card_down(card_item):
    card_id, image, parameters = card_item
    canvas.move(card_id, 0, 5)  # Move the card down by 5 pixels

    # Schedule a callback to move the card back to its original position after a delay
    canvas.after(100, move_card_up, card_item)

# Function to move the card back to its original position
def move_card_up(card_item):
    card_id, image, parameters = card_item
    canvas.move(card_id, 0, -5)  # Move the card back up by 5 pixels

# Function to create and display a new character card
def create_character_card(image_path, parameters):
    img = Image.open(image_path)
    resized_image = img.resize((90, 80), Image.NEAREST)
    image = ImageTk.PhotoImage(resized_image)

    # Display the character card on the canvas
    card_id = canvas.create_image(len(character_cards) * 120, 100, image=image, anchor=tk.NW)
    
    # Attach a click event handler with a unique lambda function
    canvas.tag_bind(card_id, "<Button-1>", lambda event, card_item=(card_id, image, parameters): character_card_clicked(card_item))

    # Keep a reference to the ImageTk.PhotoImage object and associated parameters
    character_cards.append((card_id, image, parameters))

# Create the main application window
root = tk.Tk()
root.title("Character Creator")

# Create a canvas to display character cards
canvas = tk.Canvas(root, width=800, height=300)
canvas.pack()

# Define the parameters for each character card
card1_parameters = ("Parameter 1 for Card 1", "Parameter 2 for Card 1")
card2_parameters = ("Parameter 1 for Card 2", "Parameter 2 for Card 2")

# Create character cards by calling create_character_card function
# Replace 'images\\TheExpanse-Earther.jpg' with the actual image file path
create_character_card("images\\TheExpanse-Earther.jpg", card1_parameters)
create_character_card("images\\Martian.jpg", card2_parameters)

root.mainloop()
