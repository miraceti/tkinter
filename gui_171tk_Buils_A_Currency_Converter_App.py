from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title('currency converter app')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')
root.resizable(True, True)  #largeur , hauteur



# create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# create 2 frame
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame=Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# add tabs
my_notebook.add(currency_frame, text= "Currencies")
my_notebook.add(conversion_frame, text= "Convert")

# disable 2nd tab
my_notebook.tab(1, state='disabled')

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("WARNING! ", "You didn't fill out all the fields")
    else:
        # disable entry boxes
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        #enable tab convert
        my_notebook.tab(1, state='normal')
        #change tab fiels
        amount_label.config(text=f'Amount of {home_entry.get()} to convert to {conversion_entry.get()}')
        converted_label.config(text=f'Equals this many {conversion_entry.get()}')
        convert_button.config(text=f'Convert from {home_entry.get()} ')

def unlock():
     # enable entry boxes
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")
    #enable tab convert
    my_notebook.tab(1, state='disabled')


#currency
home = LabelFrame(currency_frame, text="Your Home Currency")
home.pack(pady=20)

home_entry = Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10, padx=10)

# conversion currency frame
conversion = LabelFrame(currency_frame, text="Conversion Currency")
conversion.pack(pady=20)

# convert to label
conversion_label = Label(conversion, text="Currency to convert to...")
conversion_label.pack(pady=10)

# convert to Entry
conversion_entry = Entry(conversion, font=("Helvetica",24))
conversion_entry.pack(pady=10, padx=10)

# rate label
rate_label = Label(conversion, text="Curren Conversion Rate....")
rate_label.pack(pady=10)

# rate Entry
rate_entry = Entry(conversion, font=("Helvetica",24))
rate_entry.pack(pady=10, padx=10)

# button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# buttons
lock_button = Button(button_frame, text="Lock", command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="UnLock", command=unlock)
unlock_button.grid(row=0, column=1, padx=10)


# Convert
def convert():
    #clear converted entry box
    converted_entry.delete(0, END)
    
    conversion = float(rate_entry.get()) * float(amount_entry.get())
    # conversion a 2 decimales
    conversion = round(conversion,2)
    # add commas separator avec un format
    conversion = '{:,}'.format(conversion)
   
    converted_entry.insert(0, f'${conversion}')
    

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

amount_label = LabelFrame(conversion_frame, text="Amount To Convert")
amount_label.pack(pady=20)

amount_entry = Entry(amount_label, font=("helvetica", 24))
amount_entry.pack(pady=10, padx=10)

convert_button = Button(amount_label, text="Convert", command=convert)
convert_button.pack(pady=20)

# equals frame
converted_label = LabelFrame(conversion_frame, text="Converted Currency")
converted_label.pack(pady=20)

converted_entry = Entry(converted_label, font=("helvetica", 24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

# Fake label
spacer = Label(conversion_frame, text="", width=68)
spacer.pack()






root.mainloop()