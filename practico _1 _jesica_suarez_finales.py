from random import randint, uniform, random
#Esta funcion imprime hola mundo EJERCICIO 1

def imprimir ():
    print "Hola Mundo"

#imprimir()
'''
#toma dos valores, los suma y los muestra EJERCICIO 2
'''
def suma (n,m):
    return n+m

print(suma(2,3))
'''
#Muestra cual es mayor EJERCICIO 3
'''
def mayor (a,b):
    if a>b:
        print a,"Es mayor"
    elif b>a:
        print b,"Es mayor"
    else:
        print "son iguales"

mayor(8,6)
'''
#Toma un numero y verifica en que rango esta Ejercicio 4 y 5
'''
def verifica (a):
    if a>=0 and a<=10:
        return "Esta en el rango 0 a 10"
    elif a>=11 and a<=20:
        return "Esta en el rango 11 a 20"
    elif a>=21 and a<=30:
        return "Esta en el rango 21 a 30"
    else:
        return "No esta en el rango"
  
    
print (verifica(19))
'''
# Muestra los numeros del 1 al 100 con sentencia while Ejercicio 6
'''
def mostrar():
    i=1           
    while i <= 100:
        print i
        i+=1

mostrar()
'''
# Muestra los numeros del 1 al 100 con sentencia for Ejercicio 7
'''
def ver():
    for x in range(1,101):
        print x

ver()
'''
# toma un string e imprime cada uno de los caracteres Ejercicio 8
'''
def hola_mundo(a):    
    for i in range(len(a)):
        print a[i]

hola_mundo("hola mundo")
'''
# Toma un entero e imprime si es par Ejercicio 9
'''
def es_par(n):
    if n % 2==0:
        print "Es par"
    else:
        print "Es Impar"

es_par(8)
'''
# Muestra los numeros pares del 1 al 100 Ejercicio 10
'''
def pares():
    for i in range(2,101,2):
        print i

pares()
'''
# Muestra del 0 al 100 Ejercicio 11
'''
def muestra():
    for i in range(0,101):
        print i

muestra()
'''
# Imprime un numero aleatorio entre el 5 y el 10 Ejercicio 12
'''
print randint(5,10)
'''
# Genera unrango decresiente Ejercicio 13
'''
for i in range(10,-1,-1):
    print i
'''
# muestra el intercambio de los dos primeros caracteres Ejercicio 14
'''
def intercambio(s,a):
    l=s[0:2]+a[2:] +" "+ a[0:2]+s[2:]
    return l

print intercambio("HOLA","MUNDO")
'''
# toma tres numeros y devuelve el mayor de los tres Ejercicio 16
'''
def max_tres(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return "no hay numero mayor"    

print max_tres(0,2,0)
'''
# Devuelve True si es vocal y devuelve False si es consonante Ejercicio 18
'''
def vocal(b):
    if b=="a" or b=="e" or b=="i" or b=="o" or b=="u":
        return True
    elif b == "A" or b == "E" or b == "I" or b == "O" or b == "U":
        return True
    else:
        return False    


vocal("k")
'''
# Toma un parametro y devuelve True si es igual a ese numero o false caso contrario Ejercicio 15
'''
def aleatorio(n):
      if randint(1,100)==n:
        print True
      else:
        print False
    
aleatorio(89)
#Esta bien la funcion, pero la idea era hacer el juego que adivine hasta que le pegue.

'''
# Toma una lista y devuelve su longitud Ejercicio 17
'''
def longlista(l):
    if l==[]:
        return 0
    else:
        return 1 + longlista(l[1:])

print longlista([1,2])
'''
#suma los elementos de la lista, multiplica los elementos de una lista Ejercicio 19
'''
def sumalista(l):
    laSuma = 0
    for i in l:
        laSuma = laSuma + i
    return laSuma

print sumalista([5,5,5,6])

def multip(l):
    mult=1
    for i in l:
        mult=mult*i
    return mult

print multip([1,2,3,4])
'''
# Toma una una palabra y la devuelve invertida Ejercicio 20
'''
def inversa(a):
    print a[::-1]

inversa("estoy probando")    
'''
# Toma una palabra y si es palindromo devuelve True Ejercicio 21
'''
def palindromo(a):
    return a==a[::-1]

print palindromo("neuquen")
'''
# Toma dos lista y compara si tiene un mismo elemento devolvera True, Ejercicio 22 
'''
def superposicion(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                return True 
    for i in range(len(b)):
        for j in range(len(a)):
            if (a[i] == b[j]):
                return True
        else:
                return False

print superposicion([1,5,3],[4,9,0])
'''
# Toma un entero y un string y devuelve la cantidad de string que se pidio Ejercicio 23
'''
def generar_n_caracter(n,e):
       c = e
       for x in range(n-1):
            e = e + c
       print e

generar_n_caracter(6,"g")
'''
# toma una lista de numeros y imprime Ejercicio 24
'''
def procedimiento (l):
    for i in l:
        print i * "+"

procedimiento([5,1])

