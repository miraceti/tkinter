from tkinter import *
from random import randint

root=Tk()
root.title('flashcard app')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')
root.resizable(True, True)  #largeur , hauteur

words = [
    (("Hola"),("Hello")),
    (("Adiós"),("Goodbye")),
    (("Por favor"),("Please")),
    (("Gracias "),("Thank you")),
    (("Lo siento"),("Sorry")),
    (("Salud"),("Bless you (after someone sneezes)")),
    (("Sí"),("Yes")),
    (("No"),("No")),
    (("¿Quién?"),("Who")),
    (("¿Qué?"),("What")),
    (("¿Por qué?"),("Why")),
    (("¿Dónde?"),("Where"))
]

print (words[4][0])  # Lo siento
print (words[4][1])  # Sorry

#get a count of our word list
count = len(words)
print(count)

def next():
    global random_word
    global hinter, hint_count
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text="")
    hinter=""
    hint_count=0
    
    random_word = randint(0, count -1)
    spanish_word.config(text=words[random_word][0])


def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]} ")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()} ")

hinter=""
hint_count=0
def hint():
    global hint_count
    global hinter
    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1

spanish_word = Label(root, text="", font=("helvetica",36))
spanish_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry= Entry(root, font=("helvetica",18))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=10)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1, padx=10)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=2, padx=10)

close_button = Button(button_frame, text="Close")
close_button.grid(row=0, column=3, padx=10)

hint_label = Label(root, text="")
hint_label.pack(pady=20)

next()

root.mainloop()