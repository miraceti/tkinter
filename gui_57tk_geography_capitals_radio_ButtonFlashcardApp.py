from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('ERIC PY')
root.geometry("500x500")

# Fonctions
#fonction de sortie aleatoire
def random_state():
        
    #liste des etats
    global our_states
    global rando
    our_states = ['california','florida','illinois','kentucky','nebraska','nevada','newYork','oregon','texas','vermont']

    #generation d'un nombre aleatoire
    rando = randint(0, len(our_states)-1)
    state = "states/"+ our_states[rando]+".png"
    # state = "states/"+ our_states[1]+".png"

    #creation des image etats
    global state_image
    maxsize = (300, 200)
    # im = im.resize(maxsize)
    state_image = ImageTk.PhotoImage(Image.open(state).resize(maxsize))
    show_state.config(image=state_image, bg="white")
    # show_state = Label(state_frame, image=state_image)
    # show_state.pack(pady=15)


def state_answer():
    reponset = reponse.get()
    reponset = reponset.replace(" ", "_")
    

    #verification de la bonne ou mauvaise reponse
    if reponset.lower()==our_states[rando]:
        response = "Correct! " + our_states[rando].title()
    else:
        response="incorrect! " + our_states[rando].title()

    reponse_label.config(text=response)

    #effacer la zone de saisie
    reponse.delete(0, 'end')

    #on raffraichit l'image
    random_state()


def states():
    hide_all_frames()
    state_frame.pack(fill='both', expand=1)
    # my_label = Label(state_frame, text="Something").pack()


    '''
    #liste des etats
    global our_states
    global rando
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
    '''
    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady=15)
    random_state()

 
    #input box
    global reponse
    reponse = Entry(state_frame, font=("Helvetica", 18), bd=4)
    reponse.pack(pady=15)

     #un bouton de navigation
    rando_button = Button(state_frame, text="état ?", command=states).pack(pady=10)

    #un bouton de réponse
    reponse_button = Button(state_frame, text="reponse", command=state_answer)
    reponse_button.pack(pady=15)

    #label de resultat
    global reponse_label
    reponse_label = Label(state_frame, text="", font=("Helvetica", 18), bg="white")
    reponse_label.pack(pady=10)




def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill='both', expand=1)
    # my_label = Label(state_capitals_frame, text="Capitals").pack()

    global show_state
    show_state = Label(state_capitals_frame)
    show_state.pack(pady=15)

    global our_states
    our_states = ['california','florida','illinois','kentucky','nebraska','nevada','newyork','oregon','texas','vermont']

    global our_state_capitals
    our_state_capitals = {
    'california' : "sacramento",
    'florida' : "tallahassee",
    'illinois' : "spingfield",
    'kentucky' : "franckfort",
    'nebraska' : "lincoln",
    'nevada' : "carson city",
    'newyork' : "albany",
    'oregon' : "salem",
    'texas' : "austin",
    'vermont' : "montpelier"

    }

    #creation de la liste vide des reponse et du compteur
    answer_list = []
    count = 1

    #generation de 3 capitales aléatoirement
    while count < 4:
        rando = randint(0, len(our_states)-1)
        if count == 1:
            answer = our_states[rando]
            global state_image
            state = "states/"+ our_states[rando]+".png"
            maxsize = (300, 200)
            # im = im.resize(maxsize)
            state_image = ImageTk.PhotoImage(Image.open(state).resize(maxsize))
            show_state.config(image=state_image, bg="white")
        
        answer_list.append(our_states[rando])
        our_states.remove(our_states[rando])
        random.shuffle(our_states)
        count += 1

    random.shuffle(answer_list)

    global capital_radio
    capital_radio = IntVar()

    capital_radio_button1 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[0]], variable=capital_radio, value=1 ).pack()
    capital_radio_button2 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[1]], variable=capital_radio, value=2 ).pack()
    capital_radio_button3 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[2]], variable=capital_radio, value=3 ).pack()
    
    #ajout d'un bouton
    pass_button = Button(state_capitals_frame, text = "pass", command=state_capitals).pack(pady=15)



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
state_frame = Frame(root, width=500, height=500, bg="white")
state_capitals_frame = Frame(root, width=500, height=500)


root.mainloop()