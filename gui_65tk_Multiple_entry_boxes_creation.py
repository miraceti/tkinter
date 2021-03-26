from tkinter import *
from tkinter import ttk

root = Tk()
root.title('ERIC PY')
root.geometry("700x500")

my_entries = []

def something():
    entry_list =''
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'
        my_label.config(text= entry_list)

    print(my_entries[0].get())
    print(my_entries[24].get())

#row loop
for y in range(5):
        #colonne loop
    for x in range(5):
        my_entry = Entry(root)
        my_entry.grid(row=y, column=x, pady=5, padx=5)
        my_entries.append(my_entry)



my_button = Button(root, text="click", command=something)
my_button.grid(row=6, column=0,pady=20)

my_label = Label(root, text='')
my_label.grid(row=8, column=0, pady=10)



root.mainloop()