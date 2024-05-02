contatos = {"eric@gmail.com": {"nome": "Eric", "telefone": "3333-2221"}}

contatos.update({"eric@gmail.com": {"nome": "Eric"}})
print(contatos)  # {'eric@gmail.com': {'nome': 'Eric'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'eric@gmail.com': {'nome': 'Eric'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)