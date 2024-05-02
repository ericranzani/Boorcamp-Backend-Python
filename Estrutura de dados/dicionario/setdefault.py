contato = {"nome": "Eric", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Eric"
print(contato)  # {'nome': 'Eric', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Eric', 'telefone': '3333-2221', 'idade': 28