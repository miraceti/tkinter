from tkinter import *
from tkinter import ttk

root=Tk()
root.title('cursors')
root.geometry('600x600')
root.iconbitmap('ergo64.ico')
root.config(cursor="fleur")
 
 
# my_button = Button(root, text="some", cursor="star")
# my_button.pack(pady=10)

list = ["arrow", "circle","clock","cross","dotbox",
        "exchange","fleur","heart","man","mouse",
        "pirate","plus","shuttle","sizing","spider",
        "spraycan","star","target","tcross","trek"]

count = 0
row1 = 0
row2 = 0
row3 = 0
row4 = 0

for cursor in list:
    if count < 5:
        Button(root, text=cursor, cursor=cursor, width=10, height=5, fg="darkblue").grid(row=row1 , column=0, pady=10, padx=10)
        row1 += 1
        count += 1
    elif count >= 5 and count < 10:
        Button(root, text=cursor, cursor=cursor, width=10, height=5, fg="darkblue").grid(row=row2 , column=1, pady=10, padx=10)
        row2 += 1
        count += 1    
    elif count >= 10 and count < 15:
        Button(root, text=cursor, cursor=cursor, width=10, height=5, fg="darkblue").grid(row=row3 , column=2, pady=10, padx=10)
        row3 += 1
        count += 1    
    else: 
        Button(root, text=cursor, cursor=cursor, width=10, height=5, fg="darkblue").grid(row=row4 , column=3, pady=10, padx=10)
        row4 += 1
        count += 1    
         
mainloop()