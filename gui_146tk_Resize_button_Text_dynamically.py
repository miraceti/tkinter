from tkinter import *

root=Tk()
root.title('RESIZE BOUTON')
root.geometry('500x500')


Grid.columnconfigure(root, index= 0, weight=1)
Grid.rowconfigure(root, 0, weight=1)
button_1 = Button(root, text="button 1")
button_1.grid(row=0, column=0, sticky="nsew")

def resize(e):
    # on recupere la taille de l'app et on divise par 10 pour le texte
    print(e)
    size = int(e.width/10)
    # change la taille du texte
    button_1.config(font=("Helvetica",size))
    
    height_size = int(e.height/10)
    if e.height <= 300:
        button_1.config(font=("Helvetica",height_size))

# bind the app
root.bind('<Configure>', resize)

mainloop()