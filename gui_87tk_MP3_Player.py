from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('ERIC PY')
root.geometry("800x400")

#initialiser le mixer pygame
pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choisir une musique", filetypes=(("mp3 files","*.mp3"),))
    # print(song)
    song = song.replace("D:/eric/python/gui/audio/","")
    song = song.replace(".mp3","")

    song_box.insert(END, song)

def play():
    song = song_box.get(ACTIVE)
    song = f'D:/eric/python/gui/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)



#liste box playlist
song_box = Listbox(root, bg="black", fg="yellow", width=60, selectbackground="red", selectforeground="black")
song_box.pack(pady=20)


#creation player bouton image
back_btn_img = PhotoImage(file='images/back1.png')
forward_btn_img = PhotoImage(file='images/fore1.png')
play_btn_img = PhotoImage(file='images/play1.png')
pause_btn_img = PhotoImage(file='images/pause1.png')
stop_btn_img = PhotoImage(file='images/stop1.png')

#creation du frame des boutons
controls_frame = Frame(root)
controls_frame.pack(pady=20)

#creation des boutons
back_button = Button(controls_frame, image= back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img , borderwidth=0)
play_button = Button(controls_frame,image=play_btn_img , borderwidth=0, command=play)
pause_button = Button(controls_frame,image= pause_btn_img, borderwidth=0)
stop_button = Button(controls_frame,image=stop_btn_img , borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

#creation menu
my_menu = Menu(root)
root.config(menu=my_menu)

#ajout menu ajout musique
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="ajout Musique", menu=add_song_menu)
add_song_menu.add_command(label="ajouter une musique a la liste", command=add_song)


root.mainloop()