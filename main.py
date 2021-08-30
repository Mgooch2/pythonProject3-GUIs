from tkinter import *

root = Tk()

#entry widget for input box
e = Entry(root, width = 50, borderwidth = 5)#width, colorchange, borderwidth
e.pack()
e.insert(0,"Enter your Name: ")

# create function for button
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text= hello)
    myLabel.pack()


# create label widget
# myLabel1 = Label(root, text="Hello World")
# myLabel2 = Label(root, text="Hi, My name is, What")
myButton = Button(root, text="Enter your name", command = myClick, fg = "red", bg ="black")#don't add parenthesis on this function or else it won't work right
# shoving it onto screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
myButton.pack()

root.mainloop()
