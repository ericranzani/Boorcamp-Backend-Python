# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

arquivo = open('E:\Bootcamp Back-end Python\manipulando arquivos\lorem.txt')
print(arquivo.read())
arquivo.close()

arquivo = open(
    "E:\Bootcamp Back-end Python\manipulando arquivos\lorem.txt", "r"
)
print(arquivo.readline())
arquivo.close()

arquivo = open(
    "E:\Bootcamp Back-end Python\manipulando arquivos\lorem.txt", "r"
)
print(arquivo.readlines())
arquivo.close()

arquivo = open(
    "E:\Bootcamp Back-end Python\manipulando arquivos\lorem.txt", "r"
)
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()