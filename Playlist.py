from CircularDoublyLinkedList import CicularDoublyLinkedList
Playlist = CicularDoublyLinkedList()

with open("Rutas.txt","r") as file:
    for line in file:
        a = []
        a = line.split(",")
        Playlist.addnode(a[0], a[1])
        Playlist.show()
        
