from tkinter import *
import random

root = Tk()
root.title('key generator validation')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')

# generate key
def generate():
    # clear key label
    key_label.delete(0, END)
    verify_label.config(text="")
    
    # set some defaults
    key = ''
    section = '' # 4 caracteres 
    check_digit_count = 0
    alphabet='abcdefghijklmnopqrstuvwxyz1234567890'
    
    # key = aaaa-bbbb-cccc-dddd-1111  24 caracteres
    
    
    while len(key) < 25 :
        # randomly pick digit from alphabet
        char = random.choice(alphabet)
        # add random choice to key
        key += char
        # add random choice to the section
        section += char
        
        # add in the dash hyphen (-)
        if len(section)==4:
            # add -
            key += '-'
            # reset section to ''
            section = ''
    # set key to all but the last digit
    print(key)
    key = key[:-1]
    print(key)
    
    # output the key
    key_label.insert(0, key)

# create a button
generate_button = Button(root, text="Generate Key!", font=("helvetica",32), command= generate)
generate_button.pack(pady=50)

# key label
key_label = Entry(root, font=("helvetica",24), bd=0, bg="systembuttonface", width=25)
key_label.pack(pady=10, padx=50)

# verify label
verify_label = Label(root, text="waiting...", font=("helvetica",32))
verify_label.pack(pady=10) 

# score label
score_label = Label(root, text="Score : ", font=("helvetica", 32))
score_label.pack(pady=10)

root.mainloop()
