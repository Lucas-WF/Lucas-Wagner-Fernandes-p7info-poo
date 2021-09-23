# -*- coding: utf-8 -*-
"""
Código refatorado da atividade-avaliação nº3
"""


def somanprimos(n):
    a = True
    i = 1
    lista = []
    while a:
        contador = 0
        if len(lista) == n:  # Se o tamanho da lista se igualar ao valor digitado pelo usuário, o loop é terminado
            a = False
        for x in range(1, i+1):
            if i % x == 0:
                contador = contador+1
        if contador == 2:
            lista.append(i)
        i = i + 1
    return sum(lista)  # Retornando a soma dos elementos da lista


def main():
    try:
        number = int(input("Digite um número inteiro e não negativo: "))
    except:
        print("\nValor incorreto. Saindo...")
        exit()

    print(f"O resultado da soma dos {number} primeiros números primos: {somanprimos(number)}")


if __name__ == "__main__":
    main()
