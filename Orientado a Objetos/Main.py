from Pessoa import pessoa

p1 = pessoa('Iago', 20)

#p2 = pessoa('João', 25)
#p2.get_ano_nascimento()

print (p1) #imprime o lugar onde esta alocado na memoria
print (p1.nome, p1.idade)
p1.get_ano_nascimento()
print (f"ID: {pessoa.gera_id()}")
