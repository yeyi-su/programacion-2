#miLista = [1024, 3, True, 6.5] # crea una lista con elementos  
#miLista.append(False) # Agrega el elmento False por la derecha
#print(miLista) #Imprimie la lista
#miLista.insert(2,4.5) # Agrega un nuevo elemento a la lista en la posicion 2
#print(miLista) # Imprime la lista
#print(miLista.pop()) # Elimina el ultimo elemento  de la lista
#print(miLista) # Imprime la lista
#print(miLista.pop(1)) # Elimina el elemento en la posicion 1
#print(miLista) # Se imprime la lista
#miLista.pop(2) # Elimina y devuelve el elemento en la posicion 2
#print(miLista) # Se imprime la lista
#miLista.sort() # Se ordenan los elementos del mas chico al mas grande
#print(miLista) # Se imprime la lista
#miLista.reverse() # Devuelve la lista al reves
#print(miLista) # Se imprime la lista
#print(miLista.count(6.5)) # Devuelve la cantidad del mismo elementos que tiene 
#print(miLista.index(4.5)) # Devuelve el indice en que se encuentra el elemento
#miLista.remove(6.5) # Elimina el elemento de la lista
#print(miLista) # Imprime la lista
#del miLista[0] # Elimina el elmento del indice 0
#print(miLista) #imprime la lista

#a=[3,3,3,3,3,3,3,3,3]
#for i in range (9):
    #print(a[i])

# a) NO se puede ejecutar
# b) El problema esta en el rango 
# c) El error quiere decir que se esta intentando acceder a un indece de la lista que no existe

def pares(lista):
    res=0
    for i in lista:
        if i%2==0:
            res+=1
    return res
    
#print(pares([1,2,5,6]))


def sumLista(lista):
    list=0
    for x in lista:
        list = list + x
    return list

#print(sumLista([1,2,3,4]))

def multiplicaLista(lista):
    mult=1
    for i in lista:
        mult= mult * i
    return mult

#print(multiplicaLista([1,2,3,4]))

def maximoEnLista(lista):
    list=0
    for i in range(len(lista)):
        if lista[i]>list:
            list=lista[i]
    return list

#print(maximoEnL00ista([1,2,3,4,9]))

def filtrarPalabrasn(lista,n):
    for palabra in lista:
        if len(palabra)>n:
            return palabra
        
#print(filtrarPalabrasn(['mi diario python','mundo','lu'],4))
        
def almacenarVectores(a,b):
    vector=0
    for i in range(len(a)):
        vector+= a[i]*b[i]
    return vector

#print(almacenarVectores((1,2,3),(-1,0,2)))

def eliminarDuplicados(lista):
    noDuplicado= set(lista) 
    return noDuplicado

#print(eliminarDuplicados([1,2,3,4,2]))
def matrizVacia():
    matriz=[]
    for i in range(2):
        matriz.append([0]*3)
    return(matriz)

#print(matrizVacia())

