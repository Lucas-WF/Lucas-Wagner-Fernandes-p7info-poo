queue = []

a = True
while a:
    element = input("Digite um elemento para a pilha ou \'sair\' para sair: ").title()  # Laço para a adição de elementos para a pilha
    if element != "Sair":
        queue.append(element)  # Adição
    else:
        a = False  # Condição de saída

try:
    queue = list(map(int, queue))  # Caso a lista seja uma lista de strings que possa ser convertida em inteiros, trouxe a função map (questão estétitca)
except:
    pass

print("\nFila:", queue,"\n")

for i in range(len(queue)):  # Laço para a remoção de elementos da pilha
    fora = input("Gostaria de retirar um elemento? Digite S ou N: ").title()
    if fora == "S":  # Condição para a remoção
        print("Elemento retirado:", queue.pop(0))
        print(queue, "\n")
    elif fora == "N":  # Condição de saída
        break
    else:  # Caso o valor digitado não seja S ou N
        print("Digite S ou N")

print("\nA fila:", queue)
