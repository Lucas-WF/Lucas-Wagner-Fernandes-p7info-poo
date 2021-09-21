def printDecimal(dec):
    return dec  # Retorna um decimal

def printOctal(octl):
    octal = oct(octl)
    return octal  # Retorna um octal

def printHexadecimal(hexa):
    hexadecimal = hex(hexa)
    return hexadecimal  # Retorna um hexadecimal

def printBinario(binar):
    binario = bin(binar)
    return binario  # Retorna um binário

def imprimaTela(n, func1, func2, func3, func4):  # Utiliza as funções como parâmetro para retornar uma tabela organizada
    return ("""
Decimal       Octal     Hexadecimal           Binario
------------- --------- --------------------- -----------------
{:d} {:>15s} {:>9s} {:>26s}""".format(func1(n), func2(n), func3(n), func4(n)))


for i in range(0, 256):
    print(imprimaTela(i, printDecimal, printOctal, printHexadecimal, printBinario))
