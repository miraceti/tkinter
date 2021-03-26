from tkinter import *
from random import choice
from random import shuffle

root = Tk()
root.title('ERIC PY')
root.geometry("800x600")

my_label = Label(root, text="", font=("Helvetica",50))
my_label.pack(pady=10)

def shuffler():
    my_entry.delete(0,END)
    reponse_label.config(text="")

    #liste of us states
    states = ['Washington', 'Oregon', 'California', 'Ohio', 'Nebraska', 'Colorado', 'Michigan', 'Massachusetts', 'Florida', 'Texas', 'Oklahoma', 'Hawaii', 'Alaska', 'Utah', 'New Mexico', 'North Dakota', 'South Dakota', 'West Virginia', 'Virginia', 'New Jersey', 'Minnesota', 'Illinois', 'Indiana', 'Kentucky', 'Tennessee', 'Georgia', 'Alabama', 'Mississippi', 'North Carolina', 'South Carolina', 'Maine', 'Vermont', 'New Hampshire', 'Connecticut', 'Rhode Island', 'Wyoming', 'Montana', 'Kansas', 'Iowa', 'Pennsylvania', 'Maryland', 'Missouri', 'Arizona', 'Nevada', 'New York', 'Wisconsin', 'Delaware', 'Idaho', 'Arkansas', 'Louisiana']

    #on choisi un nom d'état dans la liste des états
    global word
    word = choice(states)

    # my_label.config(text=word)

    #melanger lettre nom état
    melange_lettre = list(word)
    # print(melange_lettre)

    shuffle(melange_lettre)
    # print(melange_lettre)

    #transformer les lettre melangées en mot
    global mot_melange
    mot_melange = ''
    for letter in melange_lettre:
        mot_melange += letter

    my_label.config(text=mot_melange)


def reponse():
    if word == my_entry.get():
        reponse_label.config(text="Correct")
    else:
        reponse_label.config(text="Not Correct")


my_button = Button(root, text="choisir un autre nom", command=shuffler)
my_button.pack(pady=10)

my_entry = Entry(root, font=("Helvetica",24))
my_entry.pack(pady=10)

reponse_button = Button(root, text="reponse", command=reponse)
reponse_button.pack(pady=10)

reponse_label = Label(root, text="", font=("Helvetica",18))
reponse_label.pack(pady=10)

shuffler()
root.mainloop()