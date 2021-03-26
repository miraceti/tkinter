from tkinter import *

root=Tk()
root.title('Message Widget')
root.iconbitmap('ergo64.ico')
root.geometry('500x800')

def change():
    my_message1.config(aspect = 200)


frame1 = LabelFrame(root, text = "Right justifié!")
frame1.pack(pady=20)

my_message1 = Message(frame1, text="ceci est un long text tapé au hasard pour text pour tester la justification d'un texte gauche , droite ou centré !",
                   font = ("helvetica",12),
                   aspect=150,
                   justify = RIGHT)
my_message1.pack(pady=10, padx=10)

frame2 = LabelFrame(root, text = "Left justifié!")
frame2.pack(pady=20)
my_message2 = Message(frame2, text="ceci est un long text tapé au hasard pour text pour tester la justification d'un texte gauche , droite ou centré !",
                   font = ("helvetica",18),
                   aspect=100,
                   justify = LEFT)
my_message2.pack(pady=10, padx=10)

frame3 = LabelFrame(root, text = "center justifié!")
frame3.pack(pady=20)
my_message3 = Message(frame3, text="ceci est un long text tapé au hasard pour text pour tester la justification d'un texte gauche , droite ou centré !",
                   font = ("helvetica",16),
                   aspect=200,
                   justify = CENTER)
my_message3.pack(pady=10, padx=10)

my_button = Button(root, text="Change Text", command= change)
my_button.pack(pady=20)



root.mainloop()