class Saldo:
    def __init__(self, conta: type(object), renda: int):
        self._conta = conta
        self._renda = renda

    @property
    def renda(self):
        return self._renda

    def saque(self, valor):
        if valor > self.renda:
            print("Operação Inválida!")
        elif int(valor) <= 0:
            print("Operação Inválida!")
        else:
            self._renda -= valor
            print(f"Saque de {valor} realizado!")

    def deposito(self, valor):
        if valor <= 0:
            print("Operação Inválida!")
        else:
            self._renda += valor
