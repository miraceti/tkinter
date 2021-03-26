from tkinter import *
from PIL import ImageTk, Image
from tkinter  import messagebox

root = Tk()

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showinfo("BOITE", "message RECU")
    Label(root, text=response).pack()

    if response == "ok" :
        Label(root, text="yes").pack()
    else:
        Label(root, text="no").pack()


Button(root, text="pop", command=popup).pack()



mainloop()