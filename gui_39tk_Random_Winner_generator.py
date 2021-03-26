from tkinter import *
from random import randint

root = Tk()
root.geometry("400x500")

def pick():
    entries = ['Sam','Malik','google india']

    #conversion de la liste en set  => suppression doublon
    entries_set = set (entries)
    #conversion de nouveau en liste
    unique_entries = list(entries_set)

    #creation de la taille de la liste variable
    our_number = len(unique_entries)-1
    # creation d'un nombre aleatoire entre 0 et 84
    rando =randint(0, our_number) 

    winnerLabel = Label(root, text=unique_entries[rando]  , font=("Helvetica",18))
    winnerLabel.pack(pady=50)


toplabel = Label(root, text="Win-o-rama!", font=("Helvetica",30))
toplabel.pack(pady=20)

winButton = Button(root, text="Winner BT", font=("Helvetica",30) , command=pick)
winButton.pack(pady=20)

root.mainloop()