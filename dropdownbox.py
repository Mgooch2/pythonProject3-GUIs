from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("dropdown boxes")
root.geometry("400x400")

#drop down boxes

def show():
    myLabel = Label(root, text= clicked.get()).pack()

#create list
options = [
"Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root,clicked, *options).pack()

myButton = Button(root, text="show selection", command = show)

root.mainloop()