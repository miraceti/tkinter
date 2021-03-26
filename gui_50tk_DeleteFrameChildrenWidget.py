from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu = my_menu)

def our_command():
    my_label = Label(root, text=" un menu a été sélectionné !").pack()

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    my_label = Label(file_new_frame, text=" le menu fichier + new a été sélectionné !").pack()


def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    my_label = Label(edit_cut_frame, text=" le menu edit + couper a été sélectionné !").pack()

    dummy_button = Button(edit_cut_frame,text="fauux!" ).pack(pady=10)
    child_label = Label(edit_cut_frame, text=edit_cut_frame.winfo_children())
    child_label.pack(pady=10)

    print(edit_cut_frame.winfo_children())

def hide_all_frames():
    for widget in file_new_frame.winfo_children():
        widget.destroy()

    for widget in edit_cut_frame.winfo_children():
            widget.destroy()

    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


file_menu = Menu(my_menu)
my_menu.add_cascade(label="Fichier", menu= file_menu)
file_menu.add_command(label="Nouveau", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Editer", menu= edit_menu)
edit_menu.add_command(label="Couper", command=edit_cut)
edit_menu.add_command(label="Copier", command=our_command)

option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu= option_menu)
option_menu.add_command(label="Couleurs", command=our_command)
option_menu.add_command(label="Formes", command=our_command)

file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")




root.mainloop()