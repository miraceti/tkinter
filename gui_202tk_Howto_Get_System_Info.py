from tkinter import *
import platform

root = Tk()
root.title('System info')
root.iconbitmap('ergo64.ico')
root.geometry('880x300')

info =f"System: {platform.system()}\n \
User: {platform.node()}\n \
Release: {platform.release()}\n \
Version: {platform.version}\n \
Machine: {platform.machine()}\n \
Processor: {platform.processor()}\n \
Python Version:  {platform.python_version()}\n \
"

my_label = Label(root, text=info, font=("helvetica",14))
my_label.pack(pady=20)

root.mainloop()
