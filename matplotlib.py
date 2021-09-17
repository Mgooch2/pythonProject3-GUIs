from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Charts and Graphs')
root.geometry('600x600')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()

my_button = Button(root, text="Graph it!", command=graph)
my_button.pack()

root.mainloop()