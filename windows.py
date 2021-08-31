from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Creating Windows")
root.iconbitmap('Draseart-Dumper-PokeBall.ico')


def open():
    global my_img
    top = Toplevel()
    top.title("Window 2")
    top.iconbitmap('Draseart-Dumper-PokeBall.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/tanjiro.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()
