from CircularDoublyLinkedList import CicularDoublyLinkedList
class PlayList:
    def __init__(self) -> None:
        self.Playlist = CicularDoublyLinkedList()
        with open("Rutas.txt","r") as file:
            for line in file:
                a = []
                a = line.split(",")
                self.Playlist.addnode(a[0], a[1])
            print("")
            print("LISTA CIRCULAR DOBLEMENTE ENLAZADA: ") 
            print("")   
            self.Playlist.show()
        self.p = self.Playlist.ptr
    
    def next(self):
        self.p = self.p.next
    def prev(self):
        self.p = self.p.prev

