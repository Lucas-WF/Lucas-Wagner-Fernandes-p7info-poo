"""
    Módulo itemnotafiscal 
    Classe ItemNotaFiscal 
    Atributos :
        id         - informado
        sequencial - informado
        quantidade - informado
        produto    - informado
        valor      - calculado.            
"""
from produto import Produto


class ItemNotaFiscal:
    def __init__(self, identificador, sequencial, quantidade, prodto):
        self._id = identificador
        self._sequencial = sequencial
        self._quantidade = quantidade
        self._produto = prodto
        self._descricao = self._produto.get_descricao
        self._valor_unitario = self._produto.get_valor_unitario
        self._valor_item = float(self._quantidade * self._valor_unitario)

    @property
    def get_sequencial(self):
        return self._sequencial

    @property
    def get_quantidade(self):
        return self._quantidade

    @property
    def get_descricao(self):
        return self._descricao

    @property
    def get_valor_item(self):
        return self._valor_item

    @property
    def get_valor_unit(self):
        return self._valor_unitario
      
    def str(self):
        string = "\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(
            self._valor_item, self._valor_unitario, self._descricao, self._quantidade, self._sequencial, self._id)
        return string
    
        
if __name__ == '__main__':
    produto = Produto(1, 100, 'Arroz', 5.5)
    item = ItemNotaFiscal(1, 1, 12, produto)
    print(item.str())
