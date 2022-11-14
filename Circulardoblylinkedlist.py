from Nodo import Nodo

class CicularDoublyLinkedList:
    def __init__(self):
        self.ptr = None 
        self.ult = None

    def addnode(self, rutacancion, rutaimagen):
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

    def show(self):
            p = self.ult
            print("PTR", end = "<->")
            print(p.data, end="<->")
            p = p.prev
            while(p != self.ult):
                print(p.data, end ="<->")
                p = p.prev
            print("ULT")
            
