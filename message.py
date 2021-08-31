from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Radio Buttons")
root.iconbitmap('Draseart-Dumper-PokeBall.ico')

#different types of message boxes
#showinfo(returns ok), showwarning(returns ok), showerror(returns ok), askquestion(returns yes, no), askokcancel(returns 1 0), askyesno(returns 1 0)

def popup():
    response = messagebox.askquestion("This is my Popup", "Hello, World!")
    Label(root,text=response).pack()
    # if response == "yes":
    #     Label(root, text="You clicked Yes").pack()
    # else:
    #     Label(root, text="You clicked No").pack()

Button(root, text="Popup", command=popup).pack()

mainloop()
