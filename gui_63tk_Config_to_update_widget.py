from tkinter import *

root = Tk()
root.title('ERIC PY')
root.geometry("400x400")

def something():
    my_label.config(text="new text", font=("Helvetica",12))
    root.config(bg="blue")
    my_button.config(text="configuration !", state=DISABLED, pady=30, padx=50)

global my_label
my_label = Label(root, text = "my text", font=("Helvetica",18))
my_label.pack(pady=10)

global my_button
my_button = Button(root, text="Click here", command=something)
my_button.pack(pady=10)

root.mainloop()