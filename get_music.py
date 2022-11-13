from listas_doblemente_enlazadas import CircularDoublyLinkedList
import pyglet
import os

class cancion:
    '''
    la clase cancion representa la cancion en la playlist
    esta contiene el nombre, el artista y la ruta de la misma.
    '''
    def __init__(self, name: str, artist: str, file: str) -> None:
        self.name = name
        self.artist = artist
        self.file = file

    def get_name(self) -> str:
        return self.name

    def get_artist(self) -> str:
        return self.artist

    def get_file(self) -> str:
        return self.file

    def __eq__(self, other):
        '''
        si 2 canciones tienen la misma ruta de archivos, entonces son la misma cancion.
        '''
        return self.get_file() == other.get_file()