cont_op = 0
import math
from operator import index


def fitExponencial(op):
    if op == 0: return 0
    return math.log10(op)

def calcBExpo(x1,x2,y1,y2):
    r = ( ( math.log10(y2) ) - (math.log10(y1)) ) / ( x2 - x1 )
    b = 10**r
    return b

def fibonnaci(n):
    global cont_op
    cont_op+=1

    if n <= 1: return 1
    return (fibonnaci(n-1) + fibonnaci(n-2))

#Algoritmo 2
def f(n):
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

values = []
n = []

for i in range(0,100,5):
    cont_op = 0
    print(i, f1(i), cont_op)
    n.append(i)
    values.append(cont_op)
    

y2 = values[-1]
x2 = n[-1]
for i in range(len(values)):
    if values[i] != 0:
        x1 = n[i]
        y1 = values[i]
        break
