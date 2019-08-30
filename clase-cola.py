class Cola:
    def __init__(self):
        self.items=[]
    def estavacia(self):
        return self.items==[]
    def agregar(self, item):
        self.items.insert(0, item)
    def avanzar(self):
        return self.items.pop()
    def tamano(self):
        return len(self.items)
    def imprimir(self):
        print (self.items)
    def vaciar(self):
        while not (self.estavacia()):
            self.avanzar()
    def dar_vuelta(self):
        self.items == (self.items[::-1])
        
'''Implenetacion de cola'''
#c=Cola()
#(c.agregar(6))
#(c.agregar(4))
#(c.dar_vuelta())
#(c.vaciar())
#(c.imprimir())



'''Recibe una cola mueve sus elementos a una cola nueva'''

def mover(cola):
    colaNueva=Cola()
    while not cola.estavacia():
        colaNueva.agregar(cola.avanzar())
    return colaNueva

cola=Cola()
(cola.agregar(2))
(cola.agregar(3))
(cola.agregar(9))
(cola.imprimir())
#mover(cola).imprimir()
print(cola.estavacia())


