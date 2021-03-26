from tkinter import *
from PIL import ImageTk, Image
import numpy as np 
import matplotlib.pyplot as plt

root = Tk()
root.geometry("400x400")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

my_button = Button(root, text="dessines!", command=graph).pack()

root.mainloop()