"""
  Módulo main - instancia objetos de classes definidas em
                módulos do pacote projeto01.   
"""
from produto import Produto
from cliente import Cliente
from notafiscal import NotaFiscal
from itemnotafiscal import ItemNotaFiscal


def main():
    cli = Cliente(1, "Jose Maria", 100, "200.100.345-34", 1)
    p1 = Produto(1, 100, "Arroz Agulha", 5.5)
    it1 = ItemNotaFiscal(1, 1, 10, p1)
    
    p2 = Produto(2, 200, "Feijao Mulatinho", 8.5)
    it2 = ItemNotaFiscal(2, 2, 10, p2)
    
    p3 = Produto(3, 300, "Macarao Fortaleza", 4.5)
    it3 = ItemNotaFiscal(3, 3, 10, p3)
    
    nf = NotaFiscal(1, 100, cli)
    nf.adicionar_item(it1)
    nf.adicionar_item(it2)
    nf.adicionar_item(it3)
    nf.calcular_nota_fiscal()

    print(nf.imprimir_nota_fiscal())


if __name__ == '__main__':
    main()
