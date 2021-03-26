from tkinter import *
from tkinter import ttk
import time


root = Tk()
root.title('ERIC PY')
root.geometry("800x600")

def pas():
    my_progress['value'] += 20
    my_label.config(text=my_progress['value'])
    # my_progress.start(10)
    '''
    for x in range(5):
        my_label.config(text=my_progress['value'])
        my_progress['value'] += 20
        root.update_idletasks()
        time.sleep(1)
    '''    


def stop():
    # my_progress['value'] += 20
    my_progress.stop()

my_progress =ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
my_progress.pack(pady=20)

my_button = Button(root, text="pas", command=pas)
my_button.pack(pady=20)

my_button2 = Button(root, text="stop", command=stop)
my_button2.pack(pady=20)

my_label =  Label(root, text="")
my_label.pack(pady=20)

root.mainloop()