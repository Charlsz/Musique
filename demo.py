import tkinter as tkr
from playsound import playsound
from tkinter.filedialog import askdirectory
import os

musique = tkr.Tk()
musique.title("Music Player")
musique.geometry("450x350")

def play():
    playsound("joji.mp3")

def ExitMusicPlayer():
    pass

def pause():
    playsound(None)

def unpause():
    pass

Button1 = tkr.Button(musique,width=5,height=3, font="Helvetica 12 bold",text="PLAY",command=play,bg="red",fg="white")
Button2 = tkr.Button(musique,width=5,height=3, font="Helvetica 12 bold",text="STOP",command=ExitMusicPlayer,bg="purple",fg="white")
Button3 = tkr.Button(musique,width=5,height=3, font="Helvetica 12 bold",text="PAUSE",command=pause,bg="green",fg="white")
Button4 = tkr.Button(musique,width=5,height=3, font="Helvetica 12 bold",text="UNPAUSE",command=unpause,bg="blue",fg="white")


var = tkr.StringVar()
songtitle = tkr.Label(musique, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

musique.mainloop()
