from CircularDoublyLinkedList import CicularDoublyLinkedList 
class PlayList: 
    def __init__(self) -> None:
        self.Playlist = CicularDoublyLinkedList() #in order to have access to atributes and methods of the class CicularDoublyLinkedList.

        with open("Rutas.txt","r") as file: # rutas.txt contains the songs and images routes.
            for line in file:  #goes through the file reading each line.
                a = [] 
                a = line.split(",") #splits a string into a list by specifying the separator.
                self.Playlist.addnode(a[0], a[1]) #new nodo that contains the routes info.
        self.p = self.Playlist.ptr #we locate p(contains nodo info) in the first nodo of the list(in the first song of the playlist).
                            
    
    def next(self): #moves p from the current nodo to the next (changes to the next song).
        self.p = self.p.next

    def prev(self): #moves p from the current nodo to the previous (changes to the previous song).
        self.p = self.p.prev

