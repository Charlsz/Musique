from tkinter import *
import pygame 
from PIL import ImageTk, Image
from Playlist import PlayList

class Reproductor: 

    def __init__(self) -> None:
        self.playlist = PlayList()
        self.root = Tk() 
        self.root.title('Musique') 

        self.root.geometry("1000x600") 

        pygame.mixer.init()

        self.title=Label(self.root,text="Musique", font=("calibri",20,"bold"),bg="grey",fg="white")  
        self.title.pack(side="top",fill="x")

        self.play_button = Button(self.root, text="Play Song", font=("calibri", 20), command=self.play) 
        self.play_button.pack(pady=40) 

        self.pause_button = Button(self.root, text="Pause Song", font=("Calibri", 20), command=self.pause) 
        self.pause_button.pack(pady=41)

        self.resume_button = Button(self.root, text="unpause", font=("Calibri", 20), command=self.resume)
        self.resume_button.pack(pady=42)

        self.backward_button = Button(self.root, text="Backward", font=("Calibri", 20), command=self.backward) 
        self.backward_button.pack(pady=43)

        self.forward_button = Button(self.root, text="Forward", font=("Calibri", 20), command=self.forward) 
        self.forward_button.pack(pady=43)

        self.root.mainloop()
    
    def play(self): 
        pygame.mixer.music.load(self.playlist.p.data) 
        pygame.mixer.music.play(loops=0) 
    

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()
    
    def resume(self):
        pygame.mixer.music.unpause()
    
    def backward(self):
        
        self.stop()
        self.playlist.prev()
        self.play()
        
    def forward(self):
        
        self.stop()
        self.playlist.next()
        self.play()

        #def image(self):
        #img = ImageTk.PhotoImage(Image.open("imagenes\Labilirrubina.txt"))
        #falta ubicarla en la interfaz
        #pass

    