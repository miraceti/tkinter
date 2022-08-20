from tkinter import *

#definition de l'ecran principal
root = Tk()
root.title('Tkinter.com - Button Widget!')
root.iconbitmap('ergo64.ico')
root.geometry("500x350")

def clicker():
    my_button.config(text="You click the button!")
    my_button.config(width="15")
    
#define an image
login = PhotoImage(file='images/bell1.png')

my_button = Button(root, text="Click Me! ", 
    activebackground="black",               #bg of the button active
    activeforeground="red",               #fg of the button active               
    anchor ="center",                     #position of the buuton defaut=center,n,s,e,w,se,so,ne,no
    bg = "systembuttonface",              #background
    bd ="2",                               #border
    command=clicker,                        # action of the button
    default="disabled",                             #default attribute
    disabledforeground="green",              #fg when the button is disabled
    font=("helvetica", 32),                              #font of the text
    fg="blue",                                     #foreground color
    #height="10",                            #height of the pixel image or font size
    # highlightbackground="blue",                    #color for highlight border on focus
    # highlightcolor="green",                        #color for highlight border on no focus
    # image=login,                                     #image on the button
    justify="center",                                #align text multiline
    overrelief="flat",                                     #look when mouse is over the button
    relief ="sunken",                                  #look of border groove, ridge, sunken, raised , flat
    state="normal",                               #normal, active, disabled
    takefocus=TRUE,                                  #tab from buttons ; FALSE:inactive; TRUE
    underline="3",                                    #underline text default:-1; 0:first char underline
    width="10",                                         #width of the button
    wraplength="0"                                 #if multiline one line or multiple lines 0:no wrap
    )
my_button.pack(pady=50)



#creation du mainloop utile pour tous les apps
root.mainloop()