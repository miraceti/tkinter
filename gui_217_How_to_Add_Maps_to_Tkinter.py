from tkinter import *
import tkintermapview

root = Tk()
root.title('Tkinter MapView')
root.iconbitmap('ergo64.ico')
root.geometry('1000x800')

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=880, height=700, corner_radius=0)
# set coordonates
# map_widget.set_position(36.1699, -115.1396)#vegas

# set adress
# map_widget.set_address("10 west elm street, chicago, IL, United States")
map_widget.set_address("40 avenue de l'amiral lemonnier, marly-le-roi, france")

# set zoom level
map_widget.set_zoom(17)#20 : plus près


map_widget.pack()

root.mainloop()
