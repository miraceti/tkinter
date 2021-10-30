from tkinter import *
import webbrowser

root = Tk()
root.title('Open Web Browser')
root.iconbitmap('ergo64.ico')
root.geometry('500x500')

def open_browser(e):
    # open default browser
    # webbrowser.open_new("https://google.fr")
    
    # open specific browser
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open_new("https://google.fr")
    

my_button = Button(root, text="Open Web Browser!",
                   font=("helvetica",24), 
                   command=lambda: open_browser(1))
my_button.pack(pady=50)

my_label = Label(text="open Browser", font=("helvetica", 24), fg="blue")
my_label.pack(pady=20)

my_label.bind("<Button-1>", open_browser)

root.mainloop()
