contatos = {"eric@gmail.com": {"nome": "Ericsson", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["eric@gmail.com"] = {"nome": "Eric"}

print(contatos["eric@gmail.com"])  # {"nome": "Ericsson", "telefone": "3333-2221"}

print(copia["eric@gmail.com"])  # {"nome": "Eric"}