class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.lower() #a palavra no fim define se quer maiuscula, minuscula...

    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str): #Vendo se é uma string ou um float para nao quebrar o codigo
            valor = valor.replace('R$', '')
        self._preco=valor