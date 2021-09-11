from tkinter import *
import random

root = Tk()
root.title('key generator validation')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')

# verify the key
def verify(key):
    global score
    score = 0
    
    # define the check digit
    check_digit = key[2]
    check_digit_count=0
    
    # aaaa-bbbb-cccc-dddd-1111
    # separate by dash "-"
    chunks = key.split('-')
    
    #  boucle et check
    for chunk in chunks:
        if len(chunk) != 4:
            return False
        
        for char in chunk:
            if char == check_digit:
                check_digit_count += 1
                
            #  grab the score of the anscii character
            score += ord(char) 
    
    # check for rules
    if score > 1700 and score < 1800 and check_digit_count == 3:
        return True
    else:
        return False

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
    # key_label.insert(0, key)
    # verify
    if verify(key):
        # key is verified
        key_label.insert(0, key)
        verify_label.config(text="Valid !")
        score_label.config(text=f'Score: {score}')
    else:
        # key is not verified
        # run the generate function again
        generate()

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
