from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('ERIC PY')
root.geometry("500x500")

# Fonctions
def states():
    hide_all_frames()
    state_frame.pack(fill='both', expand=1)
    my_label = Label(state_frame, text="Something").pack()

def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill='both', expand=1)
    my_label = Label(state_capitals_frame, text="Capital").pack()

#cacher les autres frames
def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget()
    state_capitals_frame.pack_forget()

#menu
my_menu = Menu(root)
root.config(menu=my_menu)

#menu details du menu geography
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="States Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

#un frame
state_frame = Frame(root, width=500, height=500)
state_capitals_frame = Frame(root, width=500, height=500)


root.mainloop()