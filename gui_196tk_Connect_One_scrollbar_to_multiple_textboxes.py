from tkinter import *

root = Tk()
root.title('one scrollbar for multiple textboxes')
root.iconbitmap('ergo64.ico')
root.geometry('600x500')

#Yview function
def multiple_yview(*args):
    my_text1.yview(*args)
    my_text2.yview(*args)
    print(*args)

#frame
my_frame = Frame(root)
my_frame.pack(pady=20)

#create scollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#textboxes
my_text1 = Text(my_frame, width=20, height=25, font=("helvetica", 16), yscrollcommand=text_scroll.set, wrap="none")
my_text1.pack(side=RIGHT, padx=5)
my_text2 = Text(my_frame, width=20, height=25, font=("helvetica", 16),yscrollcommand=text_scroll.set, wrap="none")
my_text2.pack(side=LEFT)

#configure scrollbar
text_scroll.config(command=multiple_yview)

root.mainloop()
