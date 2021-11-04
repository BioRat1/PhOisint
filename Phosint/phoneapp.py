import tkinter as tk
from tkinter import *
import phonenumbers
from phonenumbers import geocoder
from PIL import Image, ImageTk
from tkinter.font import Font
from phonenumbers import carrier



root = tk.Tk()






canvas =tk.Canvas(root, width=600, height=300, bg="#000000")
canvas.grid(columnspan=4, rowspan=4)

root.title("phOsint")

textbox = Entry(root, width=40,)
textbox.grid(column=1, row=2)




myFont = Font(
    family="Magneto",
    size=12,
    slant="roman")

logo = Image.open("anonlogorm.png",).convert("RGB")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, borderwidth=0)
logo_label.image = logo
logo_label.grid(column=1, row=0)

instructions = tk.Label(root, text="Enter in a phone number, let's see where it's located ;)", fg="light green", bg="black", font=myFont)
instructions.grid(columnspan=3, column=0, row=1)

def button_command():
    browse_text.set("As You Wish...")
    phoneNumber = phonenumbers.parse(textbox.get().strip())
    
    
    

    text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
    text_box.insert(1.0, geocoder.description_for_number(phoneNumber, "en"))
    
    
    text_box.grid(column=1, row=4)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")

    




browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=button_command, bg="purple", fg="white", height=2, width=10, font=myFont)
browse_text.set("Show Me")
browse_btn.grid(column=1, row=3)




canvas =tk.Canvas(root, width=600, height=250, bg="#000000")
canvas.grid(columnspan=3,)


root.mainloop()