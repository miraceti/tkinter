from tkinter import *
from urllib.parse import ParseResultBytes
import tkintermapview
from tkinter import ttk

root = Tk()
root.title('Tkinter MapView')
root.iconbitmap('ergo64.ico')
root.geometry('1000x800')

def recherche():
    map_widget.set_address(my_entry.get())
    my_slider.config(value=9)

def slide(e):
    map_widget.set_zoom(my_slider.get())

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=900, height=600, corner_radius=0)
# set coordonates
# map_widget.set_position(36.1699, -115.1396)#vegas

# set adress
# map_widget.set_address("10 west elm street, chicago, IL, United States")
map_widget.set_address("40 avenue de l'amiral lemonnier, marly-le-roi, france")

# set zoom level
map_widget.set_zoom(17)#20 : plus près

map_widget.pack()

my_frame = LabelFrame(root)
my_frame.pack(pady=10)

my_entry= Entry(my_frame, font=("helvetica",28))
my_entry.grid(row=0 , column=0, pady=20, padx=10)

my_button = Button(my_frame, text="Recherche", font=("helvetica",18), command=recherche)
my_button.grid(row=0, column=1, padx=10)

# my_slider = Scale(my_frame, from_ = 4, to=25, orient=HORIZONTAL, command=slide)#, value=20, length=220)
my_slider = ttk.Scale(my_frame, from_ = 4, to=25, orient=HORIZONTAL, command=slide, value=20, length=220)
my_slider.grid(row=0, column=2, padx=10)

root.mainloop()
