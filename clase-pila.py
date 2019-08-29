class Pila():
    def __init__(self):
        self.items=[]
    def estavacia(self):
        return self.items==[]
    def incluir(self,item):
        self.items.append(item)
    def inspeccionar(self):
        return self.items[len(self.items)-1]
    def extraer(self):
        return self.items.pop()
    def tamano(self):
        return len(self.items)
    def dar_vuelta(self):
        self.items == (self.items)[::-1]
    def imprimir(self):  
        print (self.items)
    def vaciar(self):
        while not (self.estavacia()):
             self.extraer()

def revertir(x):
    p=Pila()
    a=Pila()
    for i in range(len(x)):    
        p.incluir(x[i])    
    while not (p.estavacia()):
        if p.inspeccionar()!= " ":
           a.incluir(p.extraer())
        else:
            a.dar_vuelta()
            a.imprimir()
            p.extraer()
            a.vaciar()
    a.dar_vuelta()
    a.imprimir()
    
#revertir("mi diario python")


def misma_cantidad(s):
    a=Pila()
    b=Pila()
    for x in range(len(s)):
        if s[x]=="1":
            a.incluir(1)
        elif s[x]=="0":
            b.incluir(0)
    if a.tamano()== b.tamano():
        return True
    else:
        return False


#print(misma_cantidad("asd00hh1"))

def balanceado(a):
    res=True
    c=Pila()
    for i in range(len(a)):
        if a[i]=="(":
            c.incluir(a[i])
        if a[i]==")":
            if c.estavacia():
                res=False
            if not c.estavacia():
                c.extraer()
    if c.tamano()!=0:
           res=False
    return res
#print (balanceado("(()())"))
def verificar(s):
    res=True
    d=Pila()
    for i in range(len(s)):
        if s[i]=="{[(":
            d.incluir(s[i])
        if s[i]==")]}":
            if d.estavacia():
                res=False
        if not d.estavacia():
            d.extraer()
    if d.tamano()!=0:
        res=False
    return res

#print(verificar("{[)"))
def capicua(s):
    res=True
    a=Pila()
    for x in range(len(s)):
        if s==s[::-1]:
            a.incluir()
            return True
        if s!=s[::-1]:
            a.extraer()
            return False
        return res

#print(capicua("neuquen"))
    

#p=Pila()
#(p.incluir("2"))
#(p.incluir("6"))
#(p.incluir("3"))
#print(p.inspeccionar())
#print(p.extraer())
#print(p.tamano())
#(p.dar_vuelta())
#print (p)
#(p.imprimir())
#(p.vaciar())
#(p.imprimir())





class Pila2():
    def __init__(self):
          self.items=[]
    def estavacia(self):
        return self.items==[]
    def incluir(self, item):
        self.items.append(item)
    def extraer(self):
        return self.items.pop()
    def inspeccionar(self):
        return self.items[0]
    def tamano(self):
        return len(self.items)

    def imprimir(self):  
        print (self.items)
a=Pila2()
(a.incluir('hola'))
(a.incluir(23))
(a.extraer())
(a.imprimir())


