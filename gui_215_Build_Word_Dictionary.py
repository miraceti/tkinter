from tkinter import *
from PyDictionary import PyDictionary


root = Tk()
root.title('Dictionary')
root.iconbitmap('ergo64.ico')
root.geometry('600x500')

def lookup():
    # clear text box
    my_text.delete(1.0, END)
    
    # lookup word
    dictionary = PyDictionary()
    definition = dictionary.meaning(my_entry.get())
    
    # add definition to textbox
    # my_text.insert(END, definition)
    
    # fond keys and values
    for key, value in definition.items():
        # put the key header
        my_text.insert(END, key + '\n\n')
        
        for values in value:
            my_text.insert(END, f' - {values}\n\n')
    

my_label_frame = LabelFrame(root, text="Enter A Word")
my_label_frame.pack(pady=20)

my_entry = Entry(my_label_frame, font=("helvetica, 28"))
my_entry.grid(row=0, column=0, padx=10, pady=10)

my_buton = Button(my_label_frame, text="Lookup", command=lookup)
my_buton.grid(row=0, column=1, padx=10)

my_text = Text(root, height=20, width=65, wrap=WORD)
my_text.pack(pady=10)

root.mainloop()
