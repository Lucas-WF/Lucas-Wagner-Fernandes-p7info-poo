# -*- coding: utf-8 -*-
"""
Preferi a utilização de dicionários, pois a "indexação" se dá pelas chaves sendo assim,
podemos imprimir as chaves como os nomes e seus respectivos valores.
"""
words_dict = {}
nb_dict = {}  # Dicionário com palavras sem a barra de espaço
longest_word = {}

def insertPhrase(n):
    lenght_word_list = []  # Lista criada para armazenar os valores do tamanho das palavras de cada frase
    a = n.split()
    for i in a:
        b = len(i)
        lenght_word_list.append(str(b))

    str_a = (' - ').join(lenght_word_list)  # Método para separar os valores por -
    words_dict[n] = str_a 
    nbword = len(n.replace(" ",""))
    nb_dict[n] = nbword

def bigWord():  # Função para pegar a maior palavra entre todas as frases
    k = 0
    for key in words_dict.keys():
        p = key.split()
        for i in p:
            if len(i) >= k:
                k = len(i)
                longest_word = i

    return longest_word


try:
    lenght = int(input("Quantidade de palavras que gostaria de digitar: "))
except:
    print("\nO valor necessita ser inteiro")
    exit()

for i in range(lenght):  # Loop para adicionar as palavras no dicionário
    word = input("Digite algo: ")
    insertPhrase(word)
    print(" ")

print("{:<26s} | {:>10s}".format("Palavra de Entrada", "Quantidade de letras"))
print('-'*49)

for key, values in words_dict.items():  # Imprimindo as frases e seus valores separados por -
    print("{:<26s} | {:>10s}".format(key, values))
    
print('-'*49)
print(" ")

longest_word = bigWord()

z = 0
for i, j in nb_dict.items():  # Loop para pegar a maior frase entre todas as frases
    if j >= z:
        z = j
        longest = i

print(f"\nMaior frase ou palavra: {longest}")
print(f"\nA maior palavra: {longest_word}")
