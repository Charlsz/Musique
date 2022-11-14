from tkinter import *
import pygame 
pygame.mixer.init()

class Reproductor: 

    def play(): 
        pygame.mixer.music.load("Skyfullofstars.wav") 
        pygame.mixer.music.play(loops=0) 
    
    def stop():
        pygame.mixer.music.stop()
    

    def pause():
        pygame.mixer.music.pause()
    

    def resume():
        pygame.mixer.music.unpause()

    def back():
        pygame.mixer.stop()
        pygame.mixer.music.load("Skyfullofstars.wav") 
        pygame.mixer.music.play(loops=0) 

    def forward():
        pass
