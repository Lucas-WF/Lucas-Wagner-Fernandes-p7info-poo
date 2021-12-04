from models import db


class Cliente(db.Model):
    __tablename__ = "Cliente"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(125), nullable=False)
    cnpjcpf = db.Column(db.String(14), unique=True, nullable=False)
    codigo = db.Column(db.String(120), nullable=False)
    tipo = db.Column(db.Integer, nullable=False)
    nota_fiscal_id = db.Column(db.Integer, db.ForeignKey("NotaFiscal.id"), nullable=False)
    nota_fiscal = db.relationship("NotaFiscal", foreign_keys=nota_fiscal_id, backref="Cliente")

    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        super().__init__(id=id, nome=nome, codigo=codigo, cnpjcpf=cnpjcpf, tipo=tipo)

    def __repr__(self):
        return "\nID: %r, Nome %r, CNPJCPF: %r, Código: %r, Tipo: %r\n" % (self.id, self.nome, self.cnpjcpf,
                                                                           self.codigo, self.tipo)


if __name__ == "__main__":
    print("Oi")
