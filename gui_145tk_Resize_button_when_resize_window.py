from tkinter import *

root=Tk()
root.title('RESIZE BOUTON')
root.geometry('500x500')

# Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, index= 0, weight=1)
# Grid.rowconfigure(root, 1, weight=1)

button_1 = Button(root, text="button 1")
button_2 = Button(root, text="button 2")
button_3 = Button(root, text="button 3")
button_4 = Button(root, text="button 4")

button_1.grid(row=0, column=0, sticky="nsew")
button_2.grid(row=1, column=0, sticky="nsew")
button_3.grid(row=2, column=0, sticky="nsew")
button_4.grid(row=3, column=0, sticky="nsew")

button_list =[button_1, button_2, button_3, button_4]
row_number = 0
for button in button_list:
    Grid.rowconfigure(root, row_number, weight=1)
    row_number += 1


mainloop()