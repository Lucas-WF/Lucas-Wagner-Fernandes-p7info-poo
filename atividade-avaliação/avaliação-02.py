# -*- coding: utf-8 -*-
"""
Código refatorado da atividade-avaliação nº2
"""
def enumerator(phrase):  # Separa o número de caracteres por -
    word_list = []
    a = phrase.split()
    for i in a:
        word_list.append(str(len(i)))
    enum = '-'.join(word_list)
    return {phrase: enum}


def no_backspace(phrase):  # Transforma a frase em uma frase sem espaçamento
    a = phrase.replace(" ","")
    return a


def longest_phrase(words_dict):  # Retorna a maior frase entre todas as frases
    z = 0
    longest_ph = ""
    for i, j in words_dict.items():
        if len(j) >= z:
            z = len(j)
            longest_ph = i
    return longest_ph


def longest_word(phrase):  # Retorna a maior palavra da referida frase
    val = 0
    longest = ""
    for i in phrase.split():
        if len(i) >= val:
            val = len(i)
            longest = i
    return longest


def longest_word_phrase(words_list):  # Retorna a maior palavra entre todas as frases
    k = 0
    longest_word_ph = ""
    for i in words_list:
        for key, values in i.items():
            p = key.split()
            for i in p:
                if len(i) >= k:
                    k = len(i)
                    longest_word_ph = i
        return longest_word_ph


def main():  # Função principal do código
    words_dict = {}
    words_list = []
    while True:
        op = input("Palavra: ")
        if op == "0":  # Condição de saída como definido na questão
            break
        else:
            words_dict[op] = no_backspace(op)  # Dicionário para a função
            words_list.append(enumerator(op))  # Lista para a impressão e função
    print("{:<25s} | {:>20s} | {:>20s}".format("Palavra de Entrada", "Quantidade de letras", "Maior Palavra"))
    print('-' * 71)
    for i in words_list:
        for key, values in i.items():  # Imprimindo as frases, seus valores e suas maiores palavras separados por -
            print("{:<25s} | {:>20s} | {:>20s}".format(key, values, longest_word(key)))

    print(f"\nA maior frase entre todas as frases é: {longest_phrase(words_dict)}")
    print(f"\nA maior palavra entre todas as frases é: {longest_word_phrase(words_list)}")


if __name__ == "__main__":
    main()
