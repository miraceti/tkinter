from tkinter import *
from random import randint
from tkinter import ttk

root=Tk()
root.title('PAPIEr PIERRE CISEAUX!!')
root.geometry('500x500')

root.config(bg="white")

rock = PhotoImage(file='images/pierre.png')
paper = PhotoImage(file='images/papier.png')
scissors = PhotoImage(file='images/ciseaux.png')

# ajout des iamges a une liste
image_list=[rock,paper,scissors]

# pick random number entre 0 et 2
pick_number = randint(0,2)

def spin():
    pick_number = randint(0,2)
    image_label.config( image=image_list[pick_number])
    
    #  0:rock  ; 1:paper  ; 2:scissors
    
    if user_choice.get()=="Rock":
        user_choice_value = 0
    elif user_choice.get()=="Paper":
        user_choice_value = 1
    elif user_choice.get()=="Scissors":
        user_choice_value = 2
    
    # determine lose or win
    if user_choice_value == 0:
        if pick_number == 0:
            win_lose_label.config(text="Egalité")
        elif pick_number == 1:
            win_lose_label.config(text="Perdu")
        elif pick_number == 2:
            win_lose_label.config(text="Gagné")
            
    if user_choice_value == 1:
        if pick_number == 0:
            win_lose_label.config(text="Gagné")
        elif pick_number == 1:
            win_lose_label.config(text="Egalité")
        elif pick_number == 2:
            win_lose_label.config(text="Perdu")
            
    if user_choice_value == 2:
        if pick_number == 0:
            win_lose_label.config(text="Perdu")
        elif pick_number == 1:
            win_lose_label.config(text="Gagné")
        elif pick_number == 2:
            win_lose_label.config(text="Egalité")
                
            


image_label = Label(root, image=image_list[pick_number], bd=0)
image_label.pack(pady=20)
    
user_choice= ttk.Combobox(root, value=("Rock","Paper","Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

spin_button = Button(root, text="Spin!", command=spin)
spin_button.pack(pady=20)


win_lose_label = Label(root, text="", font=("Helvetica",20), bg="white")
win_lose_label.pack(pady=20)

mainloop()