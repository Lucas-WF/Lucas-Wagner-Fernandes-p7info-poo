"""
    Módulo produto
    Classe Produto
    Atributos :
        id            - informado
        codigo        - informado
        descricao     - informado
        valorUnitario - informado. 
"""


class Produto:
    def __init__(self, identificador, codigo, descricao, valor_unitario):
        self._id = identificador
        self._codigo = codigo
        self._descricao = descricao
        self._valor_unitario = valor_unitario

    @property
    def get_descricao(self):
        return self._descricao

    @property
    def get_valor_unitario(self):
        return self._valor_unitario
        
    def str(self):
        string = "\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self._valor_unitario, self._descricao,
                                                                               self._codigo, self._id)
        return string


if __name__ == '__main__':
    produto = Produto(1, 100, 'Arroz', 5.5)
    print(produto.str())
        
        
