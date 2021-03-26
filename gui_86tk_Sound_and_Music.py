from tkinter import *
import pygame

root = Tk()
root.title('ERIC PY')
root.geometry("500x400")

pygame.mixer.init()

def play():
    pygame.mixer.music.load("audio/gen1.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

my_button = Button(root, text="PLAY", font= ("Helvetica",30), command=play)
my_button.pack(pady=50)

stop_button = Button(root, text="STOP", font= ("Helvetica",30), command=stop)
stop_button.pack(pady=50)

root.mainloop()