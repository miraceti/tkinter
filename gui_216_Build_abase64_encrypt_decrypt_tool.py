from tkinter import *
import pybase64
from tkinter import messagebox

root = Tk()
root.title('Encrypt/Decrypt Base64')
root.iconbitmap('ergo64.ico')
root.geometry('600x500')


def encrypt():
    # get text from textbox
    secret = my_text.get(1.0, END)
    
    # clear the box
    my_text.delete(1.0, END)
    
    # logic for password
    if my_entry.get() == "eric":
        # convert to byte
        secret = secret.encode("ascii")
        print(secret)
        # convert to base64
        secret = pybase64.b64encode(secret)
        print(secret)
        # convert it back to ascii
        secret = secret.decode("ascii")
        print(secret)
        my_text.insert(END, secret)
    else:
        # message if wrong password
        messagebox.showwarning("Incorrect!", "Incorrect Password, Try again!")
        
    

def decrypt():
    # get text from textbox
    secret = my_text.get(1.0, END)
    
     # clear the screen
    my_text.delete(1.0, END)
    
    # logic for password
    if my_entry.get() == "eric":
        # convert to byte
        secret = secret.encode("ascii")
        print(secret)
        # convert to base64
        secret = pybase64.b64decode(secret)
        print(secret)
        # convert it back to ascii
        secret = secret.decode("ascii")
        print(secret)
        my_text.insert(END, secret)
    else:
        # message if wrong password
        messagebox.showwarning("Incorrect!", "Incorrect Password, Try again!")


def clear():
    # clear boxes
    my_text.delete(1.0, END)
    my_entry.delete(0, END)

my_frame = Frame(root)
my_frame.pack(pady=20)

enc_button =  Button(my_frame, text="Encrypt", font=("helvetica", 18), command=encrypt)
enc_button.grid(row=0, column=0)

dec_button =  Button(my_frame, text="Decrypt", font=("helvetica", 18), command=decrypt)
dec_button.grid(row=0, column=1, padx=20)

clear_button =  Button(my_frame, text="Clear", font=("helvetica", 18), command=clear)
clear_button.grid(row=0, column=2)


enc_label = Label(root, text="Encrypt/Decrypt Text...", font=("helvetica",14))
enc_label.pack()

my_text = Text(root, width=57, height=10)
my_text.pack(pady=10)

password_label = Label(root, text="Enter your password...", font=("helvetica",14))
password_label.pack()

my_entry= Entry(root, font=("helvetica", 18), width=35, show="*")
my_entry.pack(pady=10)


root.mainloop()
