from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('ERIC PY')
root.geometry("1200x650")

#creation et initialisation de la variable du fichier ouvert
global open_status_name
open_status_name = False
        
#creation de la fonction nouveau fichier
def new_file():
    my_text.delete("1.0", END)
    root.title('Nouveau fichier! - PY')
    status_bar.config(text="Nouveau Fichier   ")
    
    global open_status_name
    open_status_name = False

#creation de la fonction ouvrir fichier
def open_file():
    my_text.delete("1.0", END)
    
    #recuperer le nom du fichier exixtant
    text_file = filedialog.askopenfilename(initialdir = 'D:/eric/python/gui/', title='Ouvrir Fichier', filetypes=(("Fichiers textes", '*.txt'),('Fichiers HTML','*.html'), ('fichiers Python','*.py'), ('Tous','*.*')))
    
    #verification si on a bien ouvert un fichier
    if text_file:
        #on créé une variable globale pour le fichier
        global open_status_name
        open_status_name = text_file
    
    #mise a jour de la barre d'etat
    name = text_file
    status_bar.config(text=f'{name}         ')
    name=name.replace("D:/eric/python/gui/","")
    root.title('fichier ouvert :  ' + name)
    root.title(f'{name} - texte editeur')
    
    #ouverture du fichier
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    
    #ajout du contenu du fichier a la zone de texte
    my_text.insert(END, stuff)
    
    #fermeture du fichier ouvert
    text_file.close()

#creation de la fonction d'enregistrer sous
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir = 'D:/eric/python/gui/', title='Enregistrer le fichier sous', filetypes=(("Fichiers textes", '*.txt'),('Fichiers HTML','*.html'), ('fichiers Python','*.py'), ('Tous','*.*')))
    if text_file:
        #mise a jour de la barre d'état
        name = text_file
        status_bar.config(text=f'sauvegardé {name}         ')
        name = name.replace("D:/eric/python/gui/",'')
        root.title(f'{name} - texte editeur')
        
        #sauvegarde du fichier
        text_file=open(text_file,'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

#fonction de sauvegarde / enregistrement du fichier
def save_file():
    global open_status_name
    if open_status_name:
        #sauvegarde du fichier
        text_file=open(open_status_name,'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        #popup ou statusbar info de sauvegarde
        
        status_bar.config(text=f'sauvegardé : {open_status_name}         ')
    else:
        save_as_file()
         

# creation d'un frame principal
my_frame = Frame(root)
my_frame.pack(pady=5)

#creation de la scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#creation d'un texbox
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#configuration de la scrollbar
text_scroll.config(command= my_text.yview)

#creation d'un menu
my_menu = Menu(root )
root.config(menu=my_menu)

#ajout du menu fichier
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Nouveau", command=new_file)
file_menu.add_command(label="Ouvrir", command=open_file)
file_menu.add_command(label="Sauvegarder", command = save_file)
file_menu.add_command(label="Enregistrer Sous", command=save_as_file)

file_menu.add_separator()

file_menu.add_command(label="Quitter", command=root.quit)


#ajout d'un menu Edit
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Editer", menu=edit_menu)
edit_menu.add_command(label="Couper")
edit_menu.add_command(label="Copier")
edit_menu.add_command(label="Coller")
edit_menu.add_command(label="Annuler")
edit_menu.add_command(label="Refaire")

#ajout dune barre d'état en bas de la fenêtre
status_bar = Label(root, text="Pret        ", anchor = E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


root.mainloop()