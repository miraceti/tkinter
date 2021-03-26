from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
import win32print
import win32api

root = Tk()
root.title('ERIC PY')
root.geometry("1200x680")

#creation et initialisation de la variable du fichier ouvert
global open_status_name
open_status_name = False
global selected
selected=False
        
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
         
def cut_text(e):
    global selected
    #verification si on utilise les raccourcis clavier
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            #capture du texte a couper
            selected = my_text.selection_get()
            #effacer la partie de texte couper
            my_text.delete("sel.first", "sel.last")
            #effacer le presse papier
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_text(e):
    global selected
    
    #verification si on utilise les raccourcis clavier
    if e:
        selected = root.clipboard_get()
    
    if my_text.selection_get():
        #capture du texte a couper
        selected = my_text.selection_get()
        #effacer le presse papier
        root.clipboard_clear()
        root.clipboard_append(selected)

def paste_text(e):
    global selected
    #check si on utilise les raccourcis clavier
    if e:
        selected=root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


#bold text function
def bold_it():
    #create un font
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")
    
    #configure un tag
    my_text.tag_configure("bold", font=bold_font)
    
    #definition de current_tags
    current_tags = my_text.tag_names("sel.first")
    
    #on test si le tag est mis
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")    



#Italics text function
def italics_it():
       #create un font
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")
    
    #configure un tag
    my_text.tag_configure("italic", font=italics_font)
    
    #definition de current_tags
    current_tags = my_text.tag_names("sel.first")
    
    #on test si le tag est mis
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")    

#change couleur du texte selectionné
def text_color():
    #selection de la couleur
    my_color = colorchooser.askcolor()[1]
    
    if my_color:
        # status_bar.config(text=my_color)
        #creation de la font
        color_font = font.Font(my_text, my_text.cget("font"))
            
        #configure un tag
        my_text.tag_configure("colored", font=color_font, foreground=my_color)
        
        #definition de current_tags
        current_tags = my_text.tag_names("sel.first")
        
        #on test si le tag est mis
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")    

#change couleur de fond
def bg_color():
    #selection de la couleur
    my_color = colorchooser.askcolor()[1]
    
    if my_color:
        my_text.config(bg=my_color)

#change couleur de  tout le texte 
def all_text_color():
     #selection de la couleur
    my_color = colorchooser.askcolor()[1]
    
    if my_color:
        my_text.config(fg=my_color)

#fonction pour imprimer un fichier
def print_file():
    printer_name = win32print.GetDefaultPrinter
    status_bar.config(text=printer_name)
    
    file_to_print = filedialog.askopenfilename(initialdir = 'D:/eric/python/gui/', title='Ouvrir Fichier', filetypes=(("Fichiers textes", '*.txt'),('Fichiers HTML','*.html'), ('fichiers Python','*.py'), ('Tous','*.*')))
    
    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

#selection de tout le texte
def select_all(e):
    #ajout du tag de selecton de tout le texte
    my_text.tag_add('sel', '1.0', 'end')

#effacement de tout le  texte
def clear_all():
    my_text.delete(1.0, END)

#creation d'une barre d'outil frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)


# creation d'un frame principal
my_frame = Frame(root)
my_frame.pack(pady=5)

#creation de la scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#scroll barre horizontale
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)


#creation d'un texbox
my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

#configuration de la scrollbar
text_scroll.config(command= my_text.yview)
hor_scroll.config(command=my_text.xview)

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
file_menu.add_command(label="Imprimer fichier", command=print_file)

file_menu.add_separator()
file_menu.add_command(label="Quitter", command=root.quit)


#ajout d'un menu Edit
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Editer", menu=edit_menu)
edit_menu.add_command(label="Couper", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copier", command=lambda: copy_text(False),accelerator="(Ctrl+c)")
edit_menu.add_command(label="Coller", command=lambda: paste_text(False),accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Annuler", command=my_text.edit_undo,accelerator="(Ctrl+z)")
edit_menu.add_command(label="Refaire", command=my_text.edit_redo,accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label="Select all", command=lambda: select_all(True),accelerator="(Ctrl+a)")
edit_menu.add_command(label="Clear all", command=clear_all,accelerator="(Ctrl+y)")

#ajout d'un menu couleur
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Couleurs", menu=color_menu)
color_menu.add_command(label="selection", command=text_color)
color_menu.add_command(label="tout le texte", command=all_text_color)
color_menu.add_command(label="background", command=bg_color)


#ajout dune barre d'état en bas de la fenêtre
status_bar = Label(root, text="Pret        ", anchor = E)
status_bar.pack(fill=X, side=BOTTOM, ipady=10)

#edit bindings ou liaison
root.bind('<Control-x>', cut_text)
#root.bind('<Control-KEY-X>')
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)
#select binding
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)

fee = "ERIC LE CAM"
my_label = Label(root, text=fee[:-1]).pack()

#Creation de bouton
#Bold button
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5)

#Italics button
Italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
Italics_button.grid(row=0, column=1, padx=5)

#undo button
undo_button = Button(toolbar_frame, text="undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)

#redo button
redo_button = Button(toolbar_frame, text="redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

#text color
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)


root.mainloop()