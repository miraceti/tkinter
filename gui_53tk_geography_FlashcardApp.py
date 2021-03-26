from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title('ERIC PY')
root.geometry("500x500")

# Fonctions
def states():
    hide_all_frames()
    state_frame.pack(fill='both', expand=1)
    # my_label = Label(state_frame, text="Something").pack()

    #liste des etats
    our_states = ['alabama','alaska','arizona','arkansas','california','colorado','connecticut',
    'delaware','florida','georgia','hawaii','idaho','illinois','indiana','iowa','kansas','kentucky',
    'louisiana','maine','maryland','massachusetts','michigan','minnesota','mississippi','missouri',
    'montana','nebraska','nevada','new_hampshire','new_Jersey','new_mexico','new_York','north_carolina',
    'north_dakota','ohio','oklahoma','oregon','pennsylvania','rhode_island','south_carolina','south_dakota',
    'tennessee','Texas','utah','vermont','virginia','washington','west_virginia','wisconsin','wyoming',
    ]

    #generation d'un nombre aleatoire
    rando = randint(0, len(our_states)-1)
    state = "states/"+ our_states[rando]+".png"
    # state = "states/"+ our_states[1]+".png"

    #creation des imge etats
    global state_image
    maxsize = (300, 200)
    # im = im.resize(maxsize)
    state_image = ImageTk.PhotoImage(Image.open(state).resize(maxsize))
    show_state = Label(state_frame, image=state_image)
    show_state.pack(pady=15)

    #un bouton de navigation
    rando_button = Button(state_frame, text="état ?", command=states).pack(pady=10)


def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill='both', expand=1)
    # my_label = Label(state_capitals_frame, text="Capitals").pack()

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