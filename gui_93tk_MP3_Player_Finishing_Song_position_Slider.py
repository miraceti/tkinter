from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title('ERIC PY')
root.geometry("800x450")

#initialiser le mixer pygame
pygame.mixer.init()

def play_time():
    #verifier et arrêter une autre instance de la fonction qui tournerait encore
    if stopped:
        return
    
    current_time = pygame.mixer.music.get_pos() / 1000
    
    # capture du temps ecoulé de la musique
    # slider_label.config(text=f'slider: {int(my_slider.get())}  and song pos : {int(current_time)}')
    
    converted_current_time =time.strftime('%M:%S', time.gmtime(current_time))

    # current_song = song_box.curselection()
    song = song_box.get(ACTIVE)
    # song = song_box.get(current_song)
    
    song = f'D:/eric/python/gui/audio/{song}.mp3'

    song_mutagen = MP3(song)
    global song_length
    song_length = song_mutagen.info.length
    converted_song_length =time.strftime('%M:%S', time.gmtime(song_length))
    
    current_time += 1
    
    if int(my_slider.get())== int(song_length):
        status_bar.config(text=f'temps écoulé : {converted_song_length} sur une durée totale de {converted_song_length}   ')
    
    elif paused:
        pass
    
    elif int(my_slider.get()) == int(current_time):
        # le slider n'a pas été déplacé
            # update slider
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # le slider a été déplacé
            # update slider
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
    
        # convert to time format            #    
        converted_current_time =time.strftime('%M:%S', time.gmtime(int(my_slider.get())))
        
        # output time to status bar
        status_bar.config(text=f'temps écoulé : {converted_current_time} sur une durée totale de {converted_song_length}   ')
    
        # move this thing along by 1 sec
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)
    # status_bar.config(text=f'temps écoulé : {converted_current_time} sur une durée totale de {converted_song_length}   ')

    # my_slider.config( value=int(current_time))
    # fake_label = Label(root, text=int(current_time))
    # fake_label.pack(pady=10)
    
    
    
    status_bar.after(1000, play_time)


def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choisir une musique", filetypes=(("mp3 files","*.mp3"),))
    # print(song)
    song = song.replace("D:/eric/python/gui/audio/","")
    song = song.replace(".mp3","")

    song_box.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choisir une musique", filetypes=(("mp3 files","*.mp3"),))
    # print(song)
    # boucle d'ajout de musiques
    for song in songs:
        song = song.replace("D:/eric/python/gui/audio/","")
        song = song.replace(".mp3","")
    
        song_box.insert(END, song)



def play():
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f'D:/eric/python/gui/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    play_time()
    
    # # update slider
    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)

global stopped
stopped = False
def stop():
    # reset slider et status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    
    # stop song
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    # clear status bar
    status_bar.config(text='')
    
    # set stop variable to True
    global stopped
    stopped =  True


global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused=True

def next_song():
    # reset slider et status bar
    status_bar.config(text='')
    my_slider.config(value=0)
        
    next_one = song_box.curselection()
    # print(next_one)
    # print(next_one[0])
    next_one = next_one[0]+1
    # print(next_one)
    song = song_box.get(ACTIVE)
    # print(song)

    song = f'D:/eric/python/gui/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)

def previous_song():
    # reset slider et status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    
    next_one = song_box.curselection()
    # print(next_one)
    # print(next_one[0])
    next_one = next_one[0]-1
    # print(next_one)
    song = song_box.get(ACTIVE)
    print(song)

    song = f'D:/eric/python/gui/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)

    song_box.activate(next_one)

    song_box.selection_set(next_one, last=None)


def remove_song():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def remove_all_songs():
    stop()
    song_box.delete(0, END)
    pygame.mixer.music.stop()

def slide(x):
    # slider_label.config(text=f'{int(my_slider.get())}  of  {int(song_length)}')
    song = song_box.get(ACTIVE)
    song = f'D:/eric/python/gui/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))
    

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
back_button = Button(controls_frame, image= back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img , borderwidth=0, command=next_song)
play_button = Button(controls_frame,image=play_btn_img , borderwidth=0, command=play)
pause_button = Button(controls_frame,image= pause_btn_img, borderwidth=0, command=lambda: pause(paused))
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
add_song_menu.add_command(label="ajouter plusieurs musiques a la liste", command=add_many_songs)

remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="retirer Musique", menu=remove_song_menu)
remove_song_menu.add_command(label="retirer une musique a la liste", command=remove_song)
remove_song_menu.add_command(label="retirer toutes les musiques de la liste", command=remove_all_songs)

status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E )
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

my_slider = ttk.Scale(root, from_=0, to=100, orient =  HORIZONTAL, value=0, command=slide, length=400)
my_slider.pack(pady=30)

# slider_label = Label(root, text="0")
# slider_label.pack(pady=5)

root.mainloop()