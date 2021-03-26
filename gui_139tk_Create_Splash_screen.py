from tkinter import *

splash_root=Tk()
splash_root.title('S.P.L.A.S.H!!')
splash_root.geometry('300x200+600+350')

#hide title bar
splash_root.overrideredirect(True)

splash_label = Label(splash_root, text="Splash screen!!", font=("Helvetica", 18))
splash_label.pack(pady=20)

print("yes")
def main_window():
    splash_root.destroy()
    root = Tk()
    root.title('ERIC PY PROGRAM')
    root.geometry('500x500')
    
    main_label = Label(root, text="Main Screen", font=("Helvetica",18))
    main_label.pack(pady=20)


#splash screen timer
splash_root.after(3000, main_window)

mainloop()