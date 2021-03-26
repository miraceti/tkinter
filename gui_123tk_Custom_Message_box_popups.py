from tkinter import *
# from tkinter import messagebox

root = Tk()
root.title('ERIC PY PROGRAM')
root.geometry("600x800")
# messagebox.showinfo("Showinfo", "Information")

def choice(option):
    pop.destroy()
    
    if option=="yes":
        my_label.config(text="tu as clické YES!")
    else:
        my_label.config(text="tu as clické NO!")
    


def clicker():
    global pop
    pop = Toplevel(root)
    pop.title('popup me')
    pop.geometry("250x150")
    pop.config(bg="green")
    
    global mep
    mep = PhotoImage(file="images/2.png")
    
    pop_label = Label(pop, text="Would you like to proceed?", bg="green", fg="white", font=("Helvetica", 12))
    pop_label.pack(pady=10)
    
    my_frame = Frame(pop, bg="green")
    my_frame.pack(pady=5)
    
    me_pic = Label(my_frame, image=mep, borderwidth=0)
    me_pic.grid(row=0, column=0, padx=10)
    
    yes = Button(my_frame, text="YES", command=lambda: choice("yes"), bg="orange")
    yes.grid(row=0, column=1, padx=10)

    no = Button(my_frame, text="NO", command=lambda: choice("no"), bg="yellow")
    no.grid(row=0, column=2, padx=10)
    

my_button = Button(root, text="Click Me!", command=clicker)
my_button.pack(pady=50)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()