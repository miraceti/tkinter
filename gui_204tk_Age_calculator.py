from tkinter import *
from datetime import datetime
from tkinter import messagebox

root = Tk()
root.title('Age Calculator')
root.iconbitmap('ergo64.ico')
root.geometry('500x300')

def age():
    if my_entry.get():
        current_year = datetime.now().year
        your_age = current_year - int(my_entry.get())
        messagebox.showinfo("Your age", f"Your Age is {your_age}")
    else:
        messagebox.showerror("Error", "you forgot to enter your year")

my_label = Label(root, text="Enter your year born", font=("helvetica",24))
my_label.pack(pady=20)

my_entry = Entry(root, font=("helvetica",18))
my_entry.pack(pady=20)

my_button = Button(root, text="Calculate Age", font=("helvetica",18), command=age)
my_button.pack(pady=20)


root.mainloop()
