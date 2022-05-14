from tkinter import *
from PyDictionary import PyDictionary
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title('Dictionary')
root.iconbitmap('ergo64.ico')
root.geometry('620x470')

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
    

my_label_frame = customtkinter.CTkFrame(root, corner_radius=10)
my_label_frame.pack(pady=20)

my_entry = customtkinter.CTkEntry(my_label_frame, width=400, height=40, border_width=1, placeholder_text="Enter A Word", text_color="silver")
my_entry.grid(row=0, column=0, padx=10, pady=10)

my_buton = customtkinter.CTkButton(my_label_frame, text="Lookup", command=lookup)
my_buton.grid(row=0, column=1, padx=10)

text_frame = customtkinter.CTkFrame(root, corner_radius=10)
text_frame.pack(pady=10)

my_text = Text(text_frame, height=20, width=67, wrap=WORD, bd=0, bg="#292929", fg="silver")
my_text.pack(pady=10, padx=10)

root.mainloop()
