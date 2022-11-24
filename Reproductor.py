from tkinter import *
import pygame 
from Playlist import PlayList

class Reproductor: 

    def __init__(self) -> None:
        self.playlist = PlayList() #in order to have access to atributes and methods of the class Playlist.
        root = Tk() 
        root.title('Musique')
        root.iconbitmap('icono_musique.ico')
        root.geometry("1000x600")

        pygame.mixer.init() #initialize the mixer module

        title=Label(root,text="Musique", font=("calibri",20,"bold"),bg="grey",fg="white")  
        title.pack(side="top",fill="x")

        #interface 
        play = PhotoImage(file='play.png')
        atras = PhotoImage(file='atras.png')
        pausa = PhotoImage(file='pausa.png')
        adelante = PhotoImage(file='adelante.png')

        icono = PhotoImage(file='simbolomusica.png')
        symbol = Label(root,image=icono)
        symbol.pack()


        play_button = Button(root, image=play, font=("calibri", 20), command=self.play) 
        play_button.pack(side='left',padx=65) 

        pause_button = Button(root, image=pausa, font=("Calibri", 20), command=self.pause) 
        pause_button.pack(side='left',padx=65)

        resume_button = Button(root, text="unpause", font=("Calibri", 20), command=self.resume)
        resume_button.pack(side='left',padx=65)

        backward_button = Button(root, image=atras, font=("Calibri", 20), command=self.backward) 
        backward_button.pack(side='left',padx=65)

        forward_button = Button(root, image=adelante, font=("Calibri", 20), command=self.forward) 
        forward_button.pack(side='left',padx=65)

        root.mainloop() 
    
    def play(self): 
        pygame.mixer.music.load(self.playlist.p.data) #
        pygame.mixer.music.play(loops=0) 
    

    def stop(self):
        pygame.mixer.music.stop() #stop playback of all sound channels

    def pause(self):
        pygame.mixer.music.pause() #temporarily stop playback of all sound channels
    
    def resume(self):
        pygame.mixer.music.unpause() #resume paused playback of sound channels
    
    def backward(self): #plays the previous song
        
        self.stop()
        self.playlist.prev() 
        self.play()
        
    def forward(self): #plays the next song -+
        
        self.stop()
        self.playlist.next()
        self.play()

if __name__=="__main__":
    Reproductor()