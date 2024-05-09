# construtor
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        selfacordado = acordado

    # destrutor 
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print('auau')

def criar_cachorro():
    c = Cachorro('Bob', 'Preto', False)
    print(c.nome)


# criar_cachorro()

# cachorro = Cachorro("Rex", "Caramelo")
# cachorro.falar()