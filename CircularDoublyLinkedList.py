from Nodo import Nodo

class CicularDoublyLinkedList:  
    def __init__(self):  
        self.ptr = None #first nodo of the list
        self.ult = None #last nodo of the list
        
    def addnode(self, rutacancion, rutaimagen): #method to add a new nodo to the list
        p = Nodo(rutacancion, rutaimagen) 
        if(self.ptr==None):
            self.ptr = p
            self.ult = p
        else:
            self.ult.next = p
            p.prev = self.ult
            self.ult = p 
        self.ult.next = self.ptr
        self.ptr.prev = self.ult  
            