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

#cola=Cola()
#(cola.agregar(2))
#(cola.agregar(3))
#(cola.agregar(9))
#(cola.imprimir())
#mover(cola).imprimir()
#print(cola.estavacia())

'''Devuelve una cola nueva con los elemetos concatenados de dos colas '''


def concatenados(cola1, cola2):
    nuevaCola=Cola()
    if cola1.tamano() == cola2.tamano():
        while not cola1.estavacia():
            nuevaCola.agregar(cola1.avanzar())
            nuevaCola.agregar(cola2.avanzar())
    else:
        if cola1.tamano() > cola2.tamano():
            while not cola1.estavacia():
                nuevaCola.agregar(cola1.avanzar())
                while not cola2.estavacia():
                    nuevaCola.agregar(cola2.avanzar())
        else:
            if cola1.tamano() < cola2.tamano():
                while not cola1.estavacia():
                    nuevaCola.agregar(cola1.avanzar())
                    while not cola2.estavacia():
                        nuevaCola.agregar(cola2.avanzar())
    return nuevaCola

#cola1=Cola()
#cola2=Cola()
#cola1.agregar(1)
#cola1.agregar(2)
#cola1.agregar(3)
#cola1.agregar(12)
#cola2.agregar(4)
#cola2.agregar(5)
#cola2.agregar(6)
#cola2.agregar(7)
#cola1.imprimir()
#cola2.imprimir()
#concatenados(cola1, cola2).imprimir()

def intercambia_cola(cola1, cola2):
    acumula=Cola()
    while not cola1.estavacia():
        acumula.agregar(cola1.avanzar())
    cola1.items = cola2.items
    cola2.items = acumula.items

#cola1=Cola()
#cola2=Cola()
#cola1.agregar(5)
#cola1.agregar(9)
#cola1.agregar(3)
#cola2.agregar(7)
#cola2.agregar(8)
#cola2.agregar(11)
#cola1.imprimir()
#cola2.imprimir()
#intercambia_cola(cola1,cola2)
#cola1.imprimir()
#cola2.imprimir()



