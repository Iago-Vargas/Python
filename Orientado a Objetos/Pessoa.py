from random import randint

class pessoa:
    ano_atual = 2024

    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod #referente a classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod #é um metodo estatico, nao vai self e nem cls, somente ele
    def gera_id():
        rand = randint (1, 10)
        return rand
