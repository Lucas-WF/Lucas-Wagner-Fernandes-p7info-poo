from models import db
from models.produto import Produto


class ItemNotaFiscal(db.Model):

    __tablename__ = "ItemNotaFiscal"

    id = db.Column(db.Integer, primary_key=True)
    sequencial = db.Column(db.Integer, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey("Produto.id"), nullable=False)
    nota_fiscal_id = db.Column(db.Integer, db.ForeignKey("NotaFiscal.id"), nullable=False)
    produto = db.relationship("Produto", foreign_keys=produto_id, backref="ItemNotaFiscal")
    nota = db.relationship("NotaFiscal", foreign_keys=nota_fiscal_id, backref="ItemNotaFiscal")

    def __init__(self, id, sequencial, quantidade, produto_id, nota_fiscal_id):
        super().__init__(id=id, sequencial=sequencial, quantidade=quantidade, produto_id=produto_id, nota_fiscal_id=nota_fiscal_id)
        produto = Produto.query.filter_by(id=self.produto_id)
        self.descricao = produto[0].descricao
        self.valorUnitario = produto[0].valorunitario
        self.valorItem = self.quantidade * self.valorUnitario

    def __repr__(self):
        return "\nID: %r, Quantidade: %r, Descrição: %r, Valor Unitário: %r, Valor Item: %r\n" % (self.id,
                                                                                                  self.quantidade,
                                                                                                  self.descricao,
                                                                                                  self.valorUnitario,
                                                                                                  self.valor_item)
