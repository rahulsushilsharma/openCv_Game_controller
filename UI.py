# BASIC TKINTER CHEATSHEET
# Build basic GUIs with Python

from tkinter import *

# create blank window
window = Tk()
window.title("Welcome to LikeGeeks app")

button = Button(text = "Run")
  
button.pack()  

window.mainloop()