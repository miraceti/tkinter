from tkinter import *
from tkinter import font

root = Tk()
root.title('font chooser')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')

# create font_chooser fonction
def font_chooser(e):
    our_font.config(
        family=my_listbox.get(my_listbox.curselection())
    )

# designate default font
our_font = font.Font(family="Helvetica", size="32")

# add frame
my_frame = Frame(root, width=480, height=275)
my_frame.pack(pady=10)

# freeze frame in place
my_frame.grid_propagate(False)
my_frame.columnconfigure(0, weight=10)

# ad textbox
my_text = Text(my_frame, font= our_font)
my_text.grid(row=0, column=0)
my_text.grid_rowconfigure(0, weight=1)
my_text.grid_columnconfigure(0, weight=1)

# add list box
my_listbox = Listbox(root, selectmode=SINGLE, width=80)
my_listbox.pack()

# add font family to listbox
for f in font.families():
    my_listbox.insert('end', f)


# bind listbox
my_listbox.bind('<ButtonRelease-1>', font_chooser)

root.mainloop()
