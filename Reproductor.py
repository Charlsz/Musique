from tkinter import *
import pygame
import random

pygame.mixer.init()

lista = []
for i in range(50,200,10):
	lista.append(i)
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