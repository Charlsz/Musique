import tkinter as tkr
import winsound
from playsound import playsound
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import os

musique = tkr.Tk()
musique.title("Musique")
musique.geometry("450x350")

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def play():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    playsound('joji.mp3', winsound.SND_ASYNC)

def ExitMusicPlayer():
    pass

def stop():
    winsound.PlaySound(None, winsound.SND_PURGE)

def unpause():
    pass





Button1 = tkr.Button(musique,width=3,height=2, font="Arial",text="PLAY",command=play,bg="blue",fg="white")
Button2 = tkr.Button(musique,width=3,height=2, font="Arial",text="STOP",command=stop,bg="blue",fg="white")
Button(musique, text="Add a song", width=10, height=3, font=("Arial"), fg="Purple", bg="#21b3de", command=AddMusic).place(x="10",y="40")

Scroll = Scrollbar(musique)
Playlist = Listbox(musique, width=5,height=3, font=("Arial"), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)

var = tkr.StringVar()
songtitle = tkr.Label(musique, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill='x')
Playlist.pack(fill="x")

musique.mainloop()
