saldo = 400
saque = 300
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")