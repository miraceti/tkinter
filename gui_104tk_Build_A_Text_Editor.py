from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('ERIC PY')
root.geometry("1200x650")

# creation d'un frame principal
my_frame = Frame(root)
my_frame.pack(pady=5)

#creation de la scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#creation d'un texbox
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#configuration de la scrollbar
text_scroll.config(command= my_text.yview)

#creation d'un menu
my_menu = Menu(root )
root.config(menu=my_menu)

#ajout du menu fichier
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")

file_menu.add_separator()

file_menu.add_command(label="Exit", command=root.quit)


#ajout d'un menu Edit
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Editer", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#ajout dune barre d'état en bas de la fenêtre
status_bar = Label(root, text="Pret   ", anchor = E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


root.mainloop()