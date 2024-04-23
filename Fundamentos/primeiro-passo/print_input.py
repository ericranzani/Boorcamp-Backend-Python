nome = input("Qual é o seu nome: ")
idade = input("E qual é a sua idade: ")

print(nome, idade) # eric 29
print(nome, idade, end="...\n") # eric 29...
print(nome, idade, sep="#", end="...\n") # eric#29...
print(nome, idade, sep="#") # eric#29
