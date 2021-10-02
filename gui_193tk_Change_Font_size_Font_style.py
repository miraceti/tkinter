from tkinter import *
from tkinter import font

root = Tk()
root.title('font chooser')
root.iconbitmap('ergo64.ico')
root.geometry('540x500')

# create font_chooser fonction
def font_chooser(e):
    our_font.config(
        family=my_listbox.get(my_listbox.curselection())
    )

# create font_size fonction
def font_size_chooser(e):
    our_font.config(
        size=font_size_listbox.get(font_size_listbox.curselection())
    )

# create font_style_chooser fonction
def font_style_chooser(e):
    style = font_style_listbox.get(font_style_listbox.curselection()).lower()
    print(style)
    
    if style == "bold":
        our_font.config(weight= style)
    
    if style == "regular":
        our_font.config(weight= "normal", slant="roman", underline=0, overstrike=0)
        
    if style == "italic":
        our_font.config(slant=style)
    
    if style == "bold/italic":
        our_font.config(weight="bold", slant="italic")
        
    if style == "underline":
        our_font.config(underline=1)
        
    if style == "strike":
        our_font.config(overstrike=1)
         
    

# designate default font
our_font = font.Font(family="Helvetica", size="32")

# add frame
my_frame = Frame(root, width=510, height=275)
my_frame.pack(pady=10)

# freeze frame in place
my_frame.grid_propagate(False)
my_frame.columnconfigure(0, weight=10)

# ad textbox
my_text = Text(my_frame, font= our_font)
my_text.grid(row=0, column=0)
my_text.grid_rowconfigure(0, weight=1)
my_text.grid_columnconfigure(0, weight=1)

# bottom frame
bottom_frame = Frame(root)
bottom_frame.pack()

# add labels
font_label = Label(bottom_frame, text="Choose Font", font=("helvetica",14))
font_label.grid(row=0, column=0, padx=10, sticky=W)


size_label = Label(bottom_frame, text="Font size", font=("helvetica",14))
size_label.grid(row=0, column=1, sticky=W)

style_label = Label(bottom_frame, text="Font style", font=("helvetica",14))
style_label.grid(row=0, column=2, padx=10, sticky=W)

# add list box
my_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=40)
my_listbox.grid(row=1, column=0, padx=10)

# size list box
font_size_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=20)
font_size_listbox.grid(row=1, column=1)

# style list box
font_style_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=80)
font_style_listbox.grid(row=1, column=2, padx=10)


# add font family to listbox
for f in font.families():
    my_listbox.insert('end', f)
    
# add sizes to size_listbox
font_sizes = [8, 10, 12, 14, 16, 18, 20, 36, 48]
for size in font_sizes:
    font_size_listbox.insert('end', size)
    

# add styles to style listbox
font_styles = ["Regular", "Bold", "Italic", "Bold/Italic", "Underline", "Strike"]
for style in font_styles:
    font_style_listbox.insert('end', style)


# bind listbox
my_listbox.bind('<ButtonRelease-1>', font_chooser)
font_size_listbox.bind('<ButtonRelease-1>', font_size_chooser)
font_style_listbox.bind('<ButtonRelease-1>', font_style_chooser)


root.mainloop()
