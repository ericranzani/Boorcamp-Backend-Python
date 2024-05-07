# João tem uma bicicleta e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe:
# cor, modelo, ano e valor da bicicleta vendida.
# um bicicleta pode:
# buzinar, parar e correr. Adicione esses comportamentos!
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 

    def buzinar(self):
        print("Plim Plim!")

    def parar(self):
        print('parando a bicicleta...')
        print('Bicicleta parou!')

    def pedalar(self):
        print('Vruummmm...')

    # def __str__(self):
        # return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}

    # returnar dinâmico
    def __str__(self):
        return f"{self.__class__.__name__}: {''.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" 


bike1 = Bicicleta('vermelha', 'caloi', 2024, 600)
bike1.buzinar()
bike1.parar()
bike1.pedalar()
print(bike1.cor, bike1.modelo, bike1.ano, bike1.valor) 

bike2 = Bicicleta('verde', 'monark', 2000, 200)
print(bike2)


