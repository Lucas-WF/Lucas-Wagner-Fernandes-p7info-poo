stack = []


a = True
while a:
    element = input("Digite um elemento para a pilha ou \'sair\' para sair: ")  # Laço para a adição de elementos para a pilha
    if element != "sair":
        stack.append(element)  # Adição
    else:
        a = False  # Condição de saída

try:
    stack = list(map(int, stack))  # Caso a lista seja uma lista de strings que possa ser convertida em inteiros, trouxe a função map (questão estétitca)
except:
    pass

print("\nPilha:", stack,"\n")

for i in range(len(stack)):  # Laço para a remoção de elementos da pilha
    fora = input("Gostaria de retirar um elemento? Digite S ou N: ").title()
    if fora == "S":  # Condição para a remoção
        print("Elemento retirado:", stack.pop())
        print(stack, "\n")
    elif fora == "N":  # Condição de saída
        print("")
        break
    else:  # Caso o valor digitado não seja S ou N
        print("Digite S ou N")

print("A pilha:", stack)
