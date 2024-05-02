contatos = {"eric@gmail.com": {"nome": "Eric", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "eric@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Eric", "telefone": "3333-2221"}
print(resultado)