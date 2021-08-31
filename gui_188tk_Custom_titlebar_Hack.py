from tkinter import *

root = Tk()
root.title('Change title bar color')
root.iconbitmap('ergo64.ico')
root.geometry('500x300')

# remove title bar
root.overrideredirect(True)


def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')
    
def quitter(e):
    root.quit()
    # root.destroy()

# create fake title bar
title_bar = Frame(root, bg="darkgreen", relief="raised", bd=0)
title_bar.pack(anchor=N,fill=X, expand=True)

# bind the title_bar
title_bar.bind("<B1-Motion>", move_app)

# create title text
title_label = Label(title_bar, text="   my awesome app", bg="darkgreen", fg="white")
title_label.pack(side = LEFT, pady=4)

# create close button on title bar
close_label = Label(title_bar, text="  X  ", bg="darkgreen", fg = "white" , relief="raised", bd=1)
close_label.pack(side = RIGHT, pady=4)
close_label.bind("<Button-1>", quitter)

# create close butto,
my_button = Button(root, text="CLOSE!", font=("helvetica,32"), command=root.quit)
my_button.pack(pady=100)

root.mainloop()
