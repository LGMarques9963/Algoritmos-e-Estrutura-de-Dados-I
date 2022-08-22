cont_op = 0
import math
from operator import index
from matplotlib import pyplot as plt
import numpy as np

def fitExponencial(op):
    if op == 0: return 0
    return math.log10(op)

def calcBExpo(x1,x2,y1,y2):
    r = ( ( math.log10(y2) ) - (math.log10(y1)) ) / ( x2 - x1 )
    b = 10**r
    return b

def calcBPolinomial(x1,x2,y1,y2):
    r = ( ( math.log10(y2) ) - (math.log10(y1)) ) / ( math.log10(x2) - math.log(x1) )
    b = r
    return b

def fibonnaci(n):
    global cont_op
    cont_op+=1

    if n <= 1: return 1
    return (fibonnaci(n-1) + fibonnaci(n-2))

#Algoritmo 2
def f2(n):
    global cont_op
    res = 0
    i = 1
    j = 1
    k = 10

    for i in range(int((n/2)),n,i):
        for j in range(n+1,2*i,2):
            for k in range(int(j/2),n*i,int(k/3)):
                res = res + 2 * n
                cont_op = cont_op + 1

    return res

#Algoritmo 1
def f1(n):
    global cont_op
    res = 0;
    for i in range(1,n+1):

        for j in range(1,i*i,i+1):

            for k in range(int(i/2),n+j,2):
                            
                res = res + n-1
                cont_op+=1

    return res

# Algoritmo 3
def f3(n):
    global cont_op
    res = 0;
    k=10
    for i in range(1,n*n,2):
        for j in range(int(i/2),2*i,int(i/2+1) ):
            for k in range(j+1,n+j,int(k/2+1) ):
                res = res + abs(j-i)
                cont_op+=1

    return res

#Algoritmo 4
def f4(n):
    global cont_op
    res = 0;
    for i in range(n,n*n,2):
        for j in range(n+1,n*n,2):
            for k in range(j,2*j,2):
                res = res + 1
                cont_op+=1

    return res;
    

#Algoritmo 5
def f5(n):
    global cont_op
    res = 0
    for i in range(1,n*n,1):
        for j in range(1,i,2):
            for k in range(n+1,2*i,i*j):
                res = res + k+1
                cont_op+=1

    return res

#Algoritmo 6
def f6(n,d):
    if n < 0: return d
    return f6(n -1 , 1 - d ) + f6(n -2 , d )


def calcFunction(f,min,max,step):
    global cont_op
    n = []
    values = []
    for i in range(min,max,step):
        cont_op = 0
        print(i,f(i),cont_op)
        n.append(i)
        values.append(cont_op)
    return n,values

def printExpo(n,cont):
    y = []
    for i in cont:
        if i == 0: 
            y.append(0)
            continue
        y.append(math.log10(i))

    plt.scatter(n,y)
    plt.show()

def printPoli(n,cont):
    x = []
    y = []
    for i in n:
        if i == 0: 
            x.append(0)
            continue

        x.append(math.log10(i))

    for j in cont:
        if j == 0: 
            y.append(0)
            continue

        y.append(math.log10(j))

    plt.scatter(x,y)
    plt.show()

def save_file(algoritmo,n,cont):
    caminho = "Algoritmo " + str(algoritmo) + ".txt"
    
    for i in range(len(n)):
        a = str(n[i])
        b = str(cont[i])
        fileCompleted = open(caminho, "a+", encoding='utf-8')
        fileCompleted.write(a + ";" + b + "\n")
        fileCompleted.close

print("Algoritmo 1")
n1, cont1 = calcFunction(f1,1,100,1)
save_file(1,n1,cont1)

print("Algoritmo 2")
n2, cont2 = calcFunction(f2,1,100,1)
save_file(2,n2,cont2)

print("Algoritmo 3")
n3, cont3 = calcFunction(f3,1,100,1)
save_file(3,n3,cont3)

print("Algoritmo 4")
n4, cont4 = calcFunction(f4,1,35,1)
save_file(4,n4,cont4)

print("Algoritmo 5")
n5, cont5 = calcFunction(f5,1,100,1)
save_file(5,n5,cont5)