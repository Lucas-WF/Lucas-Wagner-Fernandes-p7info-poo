from nota_fiscal import NotaFiscal
from produto import Produto


class NotaFiscalProduto:

    def __init__(self):
        self._notasFiscais = []
        self._produtos = []

    def adicionarnotaproduto(self, nota, produto):
        if isinstance(nota, NotaFiscal) and isinstance(produto, Produto):
            self._notasFiscais.append(nota)
            self._produtos.append(produto)
