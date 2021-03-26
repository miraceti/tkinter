from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('ERIC PY')
root.geometry("500x500")

# Fonctions
#creation de card suivante
def math_random():
     #generation de nombre aleatoire
    global num_1,num_2
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    global add_image1
    global add_image2

    card1 = "D:/eric/python/gui/images/chiffres/"+ str(num_1) +".png"
    card2 = "D:/eric/python/gui/images/chiffres/"+ str(num_2) +".png"

    add_image1 = ImageTk.PhotoImage(Image.open(card1))
    add_image2 = ImageTk.PhotoImage(Image.open(card2))

    #cheon met les card sur la fenetre
    add_1.config(image=add_image1)
    # math_sign.config(text='+')
    add_2.config(image=add_image2)


#fonction de calcul addition
def answer_add():
    answer = num_1 + num_2

    if int(add_answer.get()) == answer:
        response = "Correct! " + str(num_1) + " + " + str(num_2) + " égal à " + str(answer)
    else:
        response = "Incorrect! " + str(num_1) + " + " + str(num_2) + " égal à " + str(answer) + " et non à " + str(add_answer.get())

    answer_message.config(text=response)
    add_answer.delete(0, 'end')
    math_random()



#fonctions de math addition
def add():
    hide_all_frames()
    add_frame.pack(fill="both", expand=1)

    add_label = Label(add_frame, text="addition flashcards", font=("Helvetica",28)).pack()

    pic_frame = Frame(add_frame, width=400, height=300)
    pic_frame.pack()

    #generation de nombre aleatoire
    global num_1,num_2
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    #creation de 3 labels dans le frame pic_frame
    global add_1, add_2
    add_1 = Label(pic_frame )
    add_2 = Label(pic_frame )
    math_sign = Label(pic_frame, text="+", font=("Helvetica",28))

    #grid les babel dans le pic_frame
    add_1.grid(row=0, column=0)
    math_sign.grid(row=0, column=1)
    add_2.grid(row=0, column=2)


    global add_image1
    global add_image2

    card1 = "D:/eric/python/gui/images/chiffres/"+ str(num_1) +".png"
    card2 = "D:/eric/python/gui/images/chiffres/"+ str(num_2) +".png"

    add_image1 = ImageTk.PhotoImage(Image.open(card1))
    add_image2 = ImageTk.PhotoImage(Image.open(card2))

    #cheon met les card sur la fenetre
    add_1.config(image=add_image1)
    # math_sign.config(text='+')
    add_2.config(image=add_image2)

    #creation de la boite de reponse et du bouton
    global add_answer
    add_answer = Entry(add_frame, font=("helvetica",18))
    add_answer.pack(pady=20)

    add_answer_button = Button(add_frame, text="réponse", command=answer_add)
    add_answer_button.pack(pady =5)

    global answer_message
    answer_message = Label(add_frame, text="", font= ("Helvetica", 20))
    answer_message.pack(pady=15)


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

#creation de la fonction de reponse des capitales
def state_capital_answer():
    if capital_radio.get() == our_state_capitals[answer]:
        response = "correct! " + our_state_capitals[answer].title() + " est la capitale de " + answer.title()
    else:
        response = "incorrect! " +  our_state_capitals[answer].title() + " est la capitale de " + answer.title()

    answer_label_capitals.config(text=response)






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
    global answer

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
    # capital_radio = IntVar()
    capital_radio = StringVar()
    capital_radio.set(our_state_capitals[answer_list[0]])

    capital_radio_button1 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[0]].title(), variable=capital_radio, value=our_state_capitals[answer_list[0]] ).pack()
    capital_radio_button2 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[1]].title(), variable=capital_radio, value=our_state_capitals[answer_list[1]] ).pack()
    capital_radio_button3 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[2]].title(), variable=capital_radio, value=our_state_capitals[answer_list[2]] ).pack()
    
    #ajout d'un bouton
    pass_button = Button(state_capitals_frame, text = "pass", command=state_capitals).pack(pady=15)

    #creation du bouton pour repondre
    capital_answer_button = Button(state_capitals_frame, text="Reponse", command=state_capital_answer)
    capital_answer_button.pack(pady=15)

    #creation de label de reponse
    global answer_label_capitals
    answer_label_capitals = Label(state_capitals_frame, text="", font=("Helvetica", 18) )
    answer_label_capitals.pack(pady=15)



#cacher les autres frames
def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    for widget in add_frame.winfo_children():
        widget.destroy()

    add_frame.pack_forget()
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

#menu maths
math_menu = Menu(my_menu)
my_menu.add_cascade(label="Math", menu=math_menu)
math_menu.add_command(label="Addition", command=add)

#un frame
state_frame = Frame(root, width=500, height=500, bg="white")
state_capitals_frame = Frame(root, width=500, height=500)
#addition frame
add_frame = Frame(root, width=500, height=500)


root.mainloop()