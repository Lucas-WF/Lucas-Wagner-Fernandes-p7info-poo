from models import db


class Produto(db.Model):

    __tablename__ = "Produto"

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    valorunitario = db.Column(db.Float, nullable=False)
    item = db.relationship("ItemNotaFiscal", backref='Produto')

    def __init__(self, id, codigo, descricao, valorunitario):
        super().__init__(id=id, codigo=codigo, descricao=descricao, valorunitario=valorunitario)

    def getdescricao(self):
        return self._descricao

    def getvalorunitario(self):
        return self._valorUnitario

    def __repr__(self):
        return "\n Id: %r Código: %r Descrição: %r Valor Unitário: %r" % (self.id, self.codigo, self.descricao,
                                                                          self.valorunitario)
