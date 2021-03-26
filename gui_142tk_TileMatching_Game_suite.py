from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.title('MATCH GAME!!')
root.geometry('450x460')

global winner,matches
winner = 0

matches = [1,1,2,2,3,3,4,4,5,5,6,6]

random.shuffle(matches)
print(matches)

my_frame = Frame(root)
my_frame.pack(pady=10)

count = 0
answer_list = []
answer_dict = {}

def reset():
    global matches, winner
    winner=0
    matches = [1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(matches)
    my_label.config(text=" ")
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    for button in button_list:
        button.config(text=" ", bg="SystemButtonFace", state="normal")


def win():
    my_label.config(text="YOU WIN!")
    button_list = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    for button in button_list:
        button.config(bg="yellow")

def button_click(b, number):
    global count, answer_list, answer_dict, winner
    
    if b["text"]== ' ' and count < 2:
        b["text"] = matches[number]
        
        # ajout du number a la answer_list
        answer_list.append(number)
        
        # ajout du bouton et du numbet a la answer_dict
        answer_dict[b]=matches[number]
        
        # increment du compteur
        count += 1

        print(answer_list)
        print(answer_dict)
        
    if len(answer_list)== 2 :
        if matches[answer_list[0]]== matches[answer_list[1]]:
            my_label.config(text="MATCH!")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list=[]
            answer_dict={}
            # increment du winner compteur
            winner += 1
            if winner == 6 :
                win()
        else:
            my_label.config(text="no!")
            count = 0
            answer_list=[]
            # popup box
            messagebox.showinfo("Incorrecte", "bad anwser!")
            
            # reset buttons
            for key in answer_dict:
                key["text"] = " "
            
            answer_dict={}
            

b0 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b0,0), relief="groove")
b1 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b1,1), relief="groove")
b2 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b2,2), relief="groove")
b3 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b3,3), relief="groove")
b4 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b4,4), relief="groove")
b5 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b5,5), relief="groove")
b6 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b6,6), relief="groove")
b7 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b7,7), relief="groove")
b8 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b8,8), relief="groove")
b9 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b9,9), relief="groove")
b10 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b10,10), relief="groove")
b11 = Button(my_frame, text = ' ', font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b11,11), relief="groove")

b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root, text="")
my_label.pack(pady=20)

# creation d'un menu
my_menu = Menu(root)
root.config(menu=my_menu)

# creation d'une option menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game" , command = reset)
option_menu.add_separator()
option_menu.add_command(label="Exit Game" , command = root.quit)

mainloop()