from tkinter import *

root=Tk()
root.title('switch')
root.geometry('600x600')
root.iconbitmap('ergo64.ico')

# keep track of the button status
global is_on
is_on = True

def switch():
    global is_on
    if is_on:
        on_button.config(image=off)
        my_label.config(text="The switch is OFF", fg="grey")
        is_on = False
    else:
        on_button.config(image=on)
        my_label.config(text="The switch is ON", fg="green")
        is_on = True

my_label = Label(root, text="The switch is ON", fg="green" , font=("helvetica",32))
my_label.pack(pady=20) 
 
# define our images
on = PhotoImage(file="images/on1.png")
off = PhotoImage(file="images/off1.png")
         
# create a button
on_button = Button(root, image=on , bd=0, command=switch)
on_button.pack(pady=50)
# off_button = Button(root, image=off)
# off_button.pack(pady=50)

mainloop()