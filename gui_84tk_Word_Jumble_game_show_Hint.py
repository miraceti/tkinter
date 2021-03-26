from tkinter import *
from random import choice
from random import shuffle

root = Tk()
root.title('ERIC PY')
root.geometry("800x600")

my_label = Label(root, text="", font=("Helvetica",50))
my_label.pack(pady=10)

def shuffler():

    hint_label.config(text="")

    #"un compteur d'aide"
    global hint_count
    hint_count = 0

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




def hint(count):
    global hint_count
    hint_count = count

    word_length = len(word)

    if count < word_length:
        hint_label.config(text=f'{hint_label["text"]} {word[count]}')
        hint_count +=1


my_entry = Entry(root, font=("Helvetica",24))
my_entry.pack(pady=10)

button_frame = Frame(root)
button_frame.pack(pady=20)

my_button = Button(button_frame, text="choisir un autre nom", command=shuffler)
my_button.grid(row=0, column=0, padx=10)

reponse_button = Button(button_frame, text="reponse", command=reponse)
reponse_button.grid(row=0, column=1, padx=10)

hint_button = Button(button_frame,text="Hint", command= lambda: hint(hint_count))
hint_button.grid(row=0, column=2, padx=10)

reponse_label = Label(root, text="", font=("Helvetica",18))
reponse_label.pack(pady=10)

hint_label = Label(root, text="", font=("Helvetica",18))
hint_label.pack(pady=10)

shuffler()
root.mainloop()