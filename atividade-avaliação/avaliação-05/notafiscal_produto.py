"""
"""

from notafiscal import NotaFiscal
from produto import Produto


class NotaFiscalProduto:
    def __init__(self): 
        self._notas_fiscais = []
        self._produtos = []
        
    def adicionar_nota_produto(self, nota, produto):
        if isinstance(nota, NotaFiscal) and isinstance(produto, Produto):
            self._notas_fiscais.append(nota)
            self._produtos.append(produto)
