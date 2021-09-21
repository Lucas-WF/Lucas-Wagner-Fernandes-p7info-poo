# -*- coding: utf-8 -*-
def somanprimos(n):
    a = True
    i = 1
    lista = []
    while a:
        contador = 0
        if len(lista) == n:
            a = False
        for x in range(1, i+1):
            if i % x == 0:
                contador = contador+1
        if contador == 2:
            lista.append(i)
        i = i + 1
    return sum(lista)


number = int(input("Digite um número inteiro e não negativo: "))
print(f"O resultado da soma dos {number} primeiros números primos: {somanprimos(number)}")
