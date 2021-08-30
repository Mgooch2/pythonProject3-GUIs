from tkinter import *

root = Tk()


# create function for button
def myClick():
    myLabel = Label(root, text="Look! i clicked button")
    myLabel.pack()


# create label widget
# myLabel1 = Label(root, text="Hello World")
# myLabel2 = Label(root, text="Hi, My name is, What")
myButton = Button(root, text="Click Me", command = myClick, fg = "red", bg ="black")#don't add parenthesis on this function or else it won't work right
# shoving it onto screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
myButton.pack()

root.mainloop()
