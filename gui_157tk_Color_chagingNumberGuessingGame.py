from tkinter import *
from random import randint

root=Tk()
root.title('Liste déroulante!')
root.geometry('500x500')

def guesser():
    if guess_box.get().isdigit():
        num_label.config(text="pick a number entre 1 et 10!")
        #trouver commenr on est moin du nombre
        dif = abs(num - int(guess_box.get()))
        if int(guess_box.get())== num:
            bc="SystemButtonFace"
            num_label.config(text =  "Correct!")
        elif dif == 5:
            bc = "white"
        elif dif < 5:
            bc=f'#ff{dif}{dif}{dif}{dif}'
        else:
            bc=f'#{dif}{dif}{dif}{dif}ff'
    else:
        guess_box.delete(0, END)
        num_label.config(text="hey ce n est pas un nombre!")
    
    root.config(bg=bc)   
    num_label.config(bg=bc) 

def rando():
    global num
    num = randint(1, 10)
    #clear the guess box
    guess_box.delete(0, END)
    num_label.config(bg="SystemButtonFace" , text="pick a number entre 1 et 10!")
    root.config(bg="SystemButtonFace")
    


num_label = Label(root, text="pick a number entre 1 et 10!" , font=("Brush Script MT",30))
num_label.pack(pady=20)

guess_box = Entry(root, font=("Helvetica", 100), width=2)
guess_box.pack(pady=20)

guess_button = Button(root, text="Submit", command=guesser)
guess_button.pack(pady=20)

rand_button = Button(root, text="Reset", command=rando)
rand_button.pack(pady=20)

# on start
rando()

mainloop()