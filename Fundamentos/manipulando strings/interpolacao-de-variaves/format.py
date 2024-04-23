# old style
# também não e muito uutilizado

nome = 'eric'
idade = 29
profissao = 'Programador'
linguagem = 'Python'

pessoa = {'nome': 'eric', 'idade': '29', 'profissao': 'Programador', 'linguagem': 'Python'} 

print("olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

# pode utilizar a posição que se quer usar os dados
print("olá, me chamo {2}. Eu tenho {3} anos de idade, trabalho como {0} e estou matriculado no curso de {1}.".format(profissao, linguagem, nome, idade ))

# passando de forma nomeada
print("olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem ))

# passando de forma nomeada
print("olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem ))

# usando dictionary
print("olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))


