from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu = my_menu)

def our_command():
    my_label = Label(root, text=" un menu a été sélectionné !").pack()

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Fichier", menu= file_menu)
file_menu.add_command(label="Nouveau", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Editer", menu= edit_menu)
edit_menu.add_command(label="Couper", command=our_command)
edit_menu.add_command(label="Copier", command=our_command)

option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu= option_menu)
option_menu.add_command(label="Couleurs", command=our_command)
option_menu.add_command(label="Formes", command=our_command)

root.mainloop()