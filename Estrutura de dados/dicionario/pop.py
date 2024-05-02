contatos = {"eric@gmail.com": {"nome": "Eric", "telefone": "3333-2221"}}

resultado = contatos.pop("eric@gmail.com")  # {'nome': 'Eric', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("eric@gmail.com", {})  # {}
print(resultado)
