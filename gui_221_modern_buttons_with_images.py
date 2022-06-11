from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title('buttons with images')
root.iconbitmap('ergo64.ico')
root.geometry('500x170')

#define Our images
add_folder_image = ImageTk.PhotoImage(Image.open("test_images/add-folder-icon.png").resize((20,20), Image.ANTIALIAS))
add_list_image = ImageTk.PhotoImage(Image.open("test_images/add-list.png").resize((20,20), Image.ANTIALIAS))

#create Our buttons
button_1 = customtkinter.CTkButton(master=root, image=add_folder_image, text="Add Folder", width=190, height=40, compound="left")
button_1.pack(pady=20, padx=20)
button_2 = customtkinter.CTkButton(master=root, image=add_list_image, text="List Folder", width=190, height=40, compound="right",
                                   fg_color="#D35B58", hover_color="#C77C78")
button_2.pack(pady=10, padx=20 )

root.mainloop()
