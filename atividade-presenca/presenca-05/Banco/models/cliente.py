class Cliente:
    def __init__(self, nome: str, endereco: str, idade: int):
        self._nome = nome
        self._endereco = endereco
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco

    @property
    def idade(self):
        return self._idade
