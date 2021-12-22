from models import db
from models.cliente import Cliente
from models.item_nota_fiscal import ItemNotaFiscal


class NotaFiscal(db.Model):

    __tablename__ = "NotaFiscal"

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey("Cliente.id"), nullable=False)
    data = db.Column(db.String(255), default="2018-11-11")
    itens = db.relationship("ItemNotaFiscal", back_populates="nota", lazy=True)
    cliente = db.relationship("Cliente", foreign_keys=cliente_id, backref="NotaFiscal")

    def __init__(self, id, codigo, cliente_id, data):
        super().__init__(id=id, codigo=codigo, cliente_id=cliente_id, data=data)

    def __repr__(self):
        return "\nID: %r, Código: %r, Cliente: %r, Data: %r QTD Itens: %r \n" % (self.id, self.codigo,
                                                                                 self.cliente.nome,
                                                                                 self.data,
                                                                                 len(self.itens))

    def get_cliente(self):
        return Cliente.query.filter_by(id=int(self.cliente_id)).first().dict()

    def get_itens(self):
        return [item for item in ItemNotaFiscal.query.filter_by(id=self.id)]

    def calcular_nota(self):
        valor = 0
        itens = self.get_itens()
        if itens:
            for item in itens:
                valor += int(item.valorItem)
            return valor

    def imprimir_nota_fiscal(self):
        primeira_linha = 111 * '-'
        espaco_cliente = ("\nNOTA FISCAL {:>99s}" + "\nCliente:{:>5s} {:>8s}: {} " + "\nCPF\\CNPJ: {}\n").format(
            self.data, self.cliente.codigo, "Nome", self.cliente.nome,
            self.cliente.cnpjcpf)

        segunda_linha = 111 * '-'
        terceira_linha = "\nITENS\n" + 111 * '-'
        espaco_crt = ("\nSEQ" + "{:>12s}" + "{:>55s}" + "{:>17s}" + "{:>17}").format("Descrição", "QTD", "Valor Unit",
                                                                                     "Preço")

        quarta_linha = ("\n" + 4 * '-' + "{:>2s}" + 56 * '-' + "{:>4s}" + 5 * '-' + "{:>5s}" + 12 * '-'
                        + "{:>5s}" + 18 * '-').format('', '', '', '')

        espaco_itens = ""
        for item in self.itens:
            espaco_itens += ("\n00{}" + "{:>20s}" + "{:>47d}" + "{:>14.2f}" + "{:>20.2f}").format(item.sequencial,
                                                                                                  item.descricao,
                                                                                                  item.quantidade,
                                                                                                  item.valorUnitario,
                                                                                                  item.valorItem)

        ultima_linha = "\n" + 111 * '_'
        nota_fiscal = (primeira_linha + espaco_cliente + segunda_linha + terceira_linha + espaco_crt + quarta_linha +
                       espaco_itens + ultima_linha + "\nValor total: " + str(self.calcular_nota()))

        return nota_fiscal
