from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ERIC PY')
root.geometry("500x400")

#  create a main frame
main_frame = Frame(root)
main_frame.pack(fill= BOTH, expand=1)

# create un canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas 
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# create  un autre frame dans le convas
second_frame = Frame(my_canvas)

#  ajouter ce nouveau frame a une windows dans ce canvas!!
my_canvas.create_window((0,0), window=second_frame, anchor="nw")


for thing in range(100):
    Button(second_frame, text =f'bouton N°{thing} top!').grid(row=thing, column=0, pady=10, padx=10)

my_label = Label(second_frame, text="coucou").grid(row=10, column=1)







root.mainloop()