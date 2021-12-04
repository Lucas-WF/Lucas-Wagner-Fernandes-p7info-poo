from models import db
from models.produto import Produto
from models.cliente import Cliente
from models.nota_fiscal import NotaFiscal
from models.item_nota_fiscal import ItemNotaFiscal


def main():
    db.create_all()

    cli = Cliente(1, "Jose Maria", 100, "200.100.345-34", 1)
    db.session.add(cli)
    db.session.commit()

    nf = NotaFiscal(1, 100, 1, 1)
    db.session.add(nf)
    db.session.commit()

    p1 = Produto(1, 100, "Arroz Agulha", 5.5)
    db.session.add(p1)
    db.session.commit()

    it1 = ItemNotaFiscal(1, 1, 10, 1, 1)
    db.session.add(it1)
    db.session.commit()

    print(nf.imprimir_nota_fiscal())


if __name__ == "__main__":
    main()
