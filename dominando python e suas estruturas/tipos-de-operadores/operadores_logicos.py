saldo = 1000
saque = 200
limite = 100

# operador E
print(saldo >= saque and saque <= limite)

# operador OU
print(saldo >= saque or saque <= limite)

# operador Negação
print(not saldo >= saque)

# com Parênteses
print(saldo >= saque and saque <= limite) or (saldo >= saque or saque <= limite)