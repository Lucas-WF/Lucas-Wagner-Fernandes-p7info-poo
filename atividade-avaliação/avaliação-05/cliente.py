"""
    Módulo cliente -
    Classe Cliente - 
    Atributos:
        _id       - chave primária    - informado
        _nome     - nome do cliente   - informado
        _codigo   - codigo do cliente - informado
        _cnpjcpf  - cnpj ou cpf       - informado
        _tipo     - tipo do cliente   - informado
                    (Pessoa Fisica ou Juridica)
        
"""

from tipocliente import TipoCliente


class Cliente:
    def __init__(self, identificador, nome, codigo, cnpjcpf, tipo):
        self._id = identificador
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf
        self._tipo = tipo

    @property
    def get_nome(self):
        return self._nome

    @property
    def get_codigo(self):
        return self._codigo

    @property
    def get_cnpjcpf(self):
        return self._cnpjcpf

    @property
    def get_id(self):
        return self._id

    def str(self):
        string = "\nId={4} Codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self._tipo, self._cnpjcpf, self._codigo,
                                                                             self._nome, self._id)
        return string


if __name__ == '__main__':
    cliente = Cliente(1, "Jose Maria", 100, '200.100.345-34', TipoCliente.PESSOA_FISICA)
    print(cliente.str())
        
    
