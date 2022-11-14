from tkinter import *
import pygame 

root = Tk() 
root.title('Musique') 

root.geometry("1000x600") 

pygame.mixer.init()

title=Label(root,text="Musique", font=("calibri",20,"bold"),bg="grey",fg="white")  
title.pack(side="top",fill="x") 

class Reproductor: 

    def play(): 
        pygame.mixer.music.load("Skyfullofstars.wav") 
        pygame.mixer.music.play(loops=0) 
    play_button = Button(root, text="Play Song", font=("calibri", 20), command=play) 
    play_button.pack(pady=40) 

    def stop():
        pygame.mixer.music.stop()
    stop_button = Button(root, text="Stop Song", font=("calibri", 20), command=stop) 
    stop_button.pack(pady=42)

    def pause():
        pygame.mixer.music.pause()
    pause_button = Button(root, text="Pause Song", font=("Calibri", 20), command=pause) 
    pause_button.pack(pady=44)

    def resume():
        pygame.mixer.music.unpause()
    resume_button = Button(root, text="Resume Song", font=("Calibri", 20), command=resume) 
    resume_button.pack(pady=46)

    def backwards():
        pass

    def forward():
        pass

root.mainloop()
