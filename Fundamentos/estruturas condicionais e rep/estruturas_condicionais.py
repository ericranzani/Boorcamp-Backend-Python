MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Qual é a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH!")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas")
else:
    print("Menor de idade, você não pode fazer a CNH!") 
