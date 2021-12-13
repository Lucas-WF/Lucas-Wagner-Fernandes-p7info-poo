class Conta:
    def __init__(self, cliente: type(object)):
        self.cliente = cliente
        self.user = cliente.nome.lower()
        self.senha = f"{cliente.nome.lower()}"+f"{cliente.idade}"+"###"

    def login(self, usuario, senha):
        if usuario == self.user and senha == self.senha:
            print("Você está logado com sucesso!")
            return "Access"
        elif usuario != self.user or senha != self.senha:
            print("\nO nome de usuário ou senha foram digitados errados!")
            return "Try Again"

    @staticmethod
    def sair(sair):
        sair = False
        return sair
