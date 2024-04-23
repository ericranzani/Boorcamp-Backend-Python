curso = 'Python'

# tranforma tudo em Maiusculo
print(curso.upper())

# tranforma tudo em Minusculo
print(curso.lower())

# tranforma so a primeira letra em maiusculo
print(curso.title())

texto = '  Olá Mundo!  '

# centralização
print(texto.center(10, "#"))

# junção
print(".".join(texto))

# corta espaço em branco
print(texto.strip() + '.')

# corta espaço em branco da direita
print(texto.rstrip() + '.')

# corta espaço em branco da esquerda
print(texto.lstrip() + '.')

menu = 'Curso em Python'
print(menu.center(23, '#'))
