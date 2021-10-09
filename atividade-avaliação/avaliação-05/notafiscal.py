"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente import Cliente
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal:
    def __init__(self, identificador, codigo, cliente):
        self._id = identificador
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.datetime.now()
        self._itens = []
        self._valor_nota = 0.0

    def set_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def adicionar_item(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcular_nota_fiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item.get_valor_item
        self._valor_nota = valor

    @property
    def get_nota(self):
        return self._valor_nota

    def imprimir_nota_fiscal(self):
        primeira_linha = 111 * '-'
        espaco_cliente = ("\nNOTA FISCAL {:>99s}" + "\nCliente:{:>5d} {:>8s}: {} " + "\nCPF\\CNPJ: {}\n").format(
                            self._data.strftime("%d/%m/%Y"), self._cliente.get_codigo, "Nome", self._cliente.get_nome,
                            self._cliente.get_cnpjcpf)

        segunda_linha = 111 * '-'
        terceira_linha = "\nITENS\n" + 111 * '-'
        espaco_crt = ("\nSEQ" + "{:>12s}" + "{:>55s}" + "{:>17s}" + "{:>17}").format("Descrição", "QTD", "Valor Unit",
                                                                                     "Preço")

        quarta_linha = ("\n" + 4 * '-' + "{:>2s}" + 56 * '-' + "{:>4s}" + 5 * '-' + "{:>5s}" + 12 * '-'
                        + "{:>5s}" + 18 * '-').format('', '', '', '')

        espaco_itens = ""
        for item in self._itens:
            espaco_itens += ("\n00{}" + "{:>20s}" + "{:>47d}" + "{:>14.2f}" + "{:>20.2f}").format(item.get_sequencial,
                                                                                                  item.get_descricao,
                                                                                                  item.get_quantidade,
                                                                                                  item.get_valor_unit,
                                                                                                  item.get_valor_item)

        ultima_linha = "\n" + 111 * '_'
        nota_fiscal = primeira_linha + espaco_cliente + segunda_linha + terceira_linha + espaco_crt + quarta_linha + \
                      espaco_itens + ultima_linha + "\nValor total: " + str(self.get_nota)

        return nota_fiscal
