contatos = {"eric@gmail.com": {"nome": "Eric", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('eric@gmail.com', {'nome': 'Eric', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError