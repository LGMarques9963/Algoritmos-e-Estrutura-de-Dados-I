from math import sqrt
from pilha import Pilha
import numpy as np

def operacoes(p,operacao):
    global tamanho_pilha
    global max_tam_pilha

    if operacao == "+":
        z1 = p.pop()
        z2 = p.pop()
        tamanho_pilha-=2
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        z = (z1[0] + z2[0], z1[1] + z2[1])
        p.push(z)
        tamanho_pilha+=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return
    
    if operacao == "-":
        z1 = p.pop()
        z2 = p.pop()
        tamanho_pilha-=2
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        z = (z1[0] - z2[0], z1[1] - z2[1])
        p.push(z)
        tamanho_pilha+=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return

    if operacao == "*":
        z1 = p.pop()
        z2 = p.pop()
        tamanho_pilha-=2
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        a = z1[0]
        b = z1[1]
        c = z2[0]
        d = z2[1]
        z = ( (a*c) - (b*d), (a*d) + (c*b))
        p.push(z)
        tamanho_pilha+=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return
    
    if operacao == "/":
        numerador = p.pop()
        denominador = p.pop()
        tamanho_pilha-=2
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        a = numerador[0]
        b = numerador[1]
        c = denominador[0]
        d = denominador[1]
        try:
            den = (c**2) + (d**2)
            div_real = ( (a*c)+ (b*d) ) / (den)
            div_imag = ( (-(a*d))+ (b*c) ) / (den)
            div = (div_real, div_imag)
            p.push(div)
            tamanho_pilha+=1
            if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        except ZeroDivisionError:
            print("Não é possível dividir por zero")
            p.push(denominador)
            p.push(numerador)
            tamanho_pilha+=2
            if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        finally:
            return

    if operacao == "chs":
        z = p.pop()
        tamanho_pilha-=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        z = (z[0] * (-1), z[1]*(-1))
        p.push(z)
        tamanho_pilha+=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return
    
    if operacao == "conj":
        z = p.pop() 
        tamanho_pilha-=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        z = (z[0], z[1]*(-1))
        p.push(z)
        tamanho_pilha+=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return

    if operacao == "inv":
        z = p.pop()
        tamanho_pilha-=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        z_real = z[0]
        z_imaginario = z[1]
        try:
            denominador = ( (z_real**2) + (z_imaginario**2))
            invz_imaginario = (-z_imaginario) / denominador
            invz_real = (z_real) / denominador
            tupla = (invz_real, invz_imaginario)
            p.push(tupla)
            tamanho_pilha+=1
            if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        except ZeroDivisionError: 
            p.push(z)
            tamanho_pilha+=1
            if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return

    if operacao == "abs":
        z = p.pop()
        tamanho_pilha-=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        mod = sqrt( (z[0]**2) + (z[1]**2))
        z = (mod, 0)
        p.push(z)
        tamanho_pilha+=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return
    
    if operacao == "pop":
        p.pop()
        tamanho_pilha-=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return

    if operacao == "swap":
        a = p.pop()
        tamanho_pilha-=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha

        if p.isempty():
            p.push(a)
            tamanho_pilha+=1
            if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
            return

        b = p.pop()
        tamanho_pilha-=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        p.push(a)
        p.push(b)
        tamanho_pilha+=2
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return

    if operacao == "dup":
        a = p.pop()
        tamanho_pilha-=1
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        p.push(a)
        p.push(a)
        tamanho_pilha+=2
        if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
        return
    


pilha = Pilha()



a = [np.genfromtxt(".\casos\caso"+str(i)+".txt", delimiter="\n", dtype = "str") for i in range(1,9)]

for j in a:
    tamanho_pilha = 0
    max_tam_pilha = 0
    for i in j:

        try:
            c,d = i.split(" ")
            tuple = (int(c),int(d))
            #print(f"Insert: {tuple}\n")
            pilha.push(tuple)
            tamanho_pilha+=1
            if tamanho_pilha>max_tam_pilha: max_tam_pilha = tamanho_pilha
            #print(f"Pilha:\n{pilha}")
            #print("\n")
        except:
            #print(f"Operacao: {i}\n")
            if i == "quit":
                break
            operacoes(pilha,i)
            #print(f"Pilha:\n{pilha}")
            #print("\n")
    
    print(pilha)
    print(f"Tamanho da Pilha: {tamanho_pilha}")
    print(f"Tamanho Máximo da Pilha: {max_tam_pilha}")
    print("\n")