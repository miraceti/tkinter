from tkinter import *
from tkinter import ttk

root=Tk()
root.title('bitmap xbm')
root.geometry('600x600')
  
# # file : .xbm
# my_button = Button(root, bitmap="error", width=40, height=40, fg='red')
# my_button.pack(pady=10)

# my_button = Button(root, bitmap="gray75", width=40, height=40, fg='red')
# my_button.pack(pady=10)

# my_button = Button(root, bitmap="gray50", width=40, height=40, fg='red')
# my_button.pack(pady=10)

# my_button = Button(root, bitmap="gray12", width=40, height=40, fg='red')
# my_button.pack(pady=10)

# my_button = Button(root, bitmap="hourglass", width=40, height=40, fg='red')
# my_button.pack(pady=10)

# my_button = Button(root, bitmap="info", width=40, height=40, fg='red')
# my_button.pack(pady=10)

# my_button = Button(root, bitmap="questhead", width=40, height=40, fg='red')
# my_button.pack(pady=10)

# my_button = Button(root, bitmap="question", width=40, height=40, fg='red')
# my_button.pack(pady=10)

# my_button = Button(root, bitmap="warning", width=40, height=40, fg='red')
# my_button.pack(pady=10)

list = ["error","gray75","gray50","hourglass","info","questhead","question","warning"]

for map in list:
    Button(root, bitmap=map, width=40, height=40, fg='darkblue').pack(pady=10)

mainloop()