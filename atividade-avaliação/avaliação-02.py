# -*- coding: utf-8 -*-
Dict = {}
Dictt = {}
longest_word = {}

def insertPhrase(n):
    Listt = []
    a = n.split()
    s = 0
    for i in a:
        b = len(i)
        Listt.append(str(b))

    str_a = (' - ').join(Listt)
    Dict[n] = str_a
    wword = len(n.replace(" ",""))
    Dictt[n] = wword

def bigWord():
    k = 0
    for key in Dict.keys():
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

for i in range(lenght):
    word = input("Digite algo: ")
    insertPhrase(word)
    print(" ")

print("{:<26s} | {:>10s}".format("Palavra de Entrada", "Quantidade de letras"))
print('-'*49)

for key, values in Dict.items():
    print("{:<26s} | {:>10s}".format(key, values))
    
print('-'*49)
print(" ")

longest_word = bigWord()

z = 0
for i, j in Dictt.items():
    if j >= z:
        z = j
        longest = i

print(f"\nMaior frase ou palavra: {longest}")
print(f"\nA maior palavra: {longest_word}")

