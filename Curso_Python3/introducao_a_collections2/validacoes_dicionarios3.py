# iremos utilizar o defaultdict
from collections import defaultdict

texto_normal = "Bem vindo meu nome é vladimir , meu filho é Davi , minha esposa Amanda e meu cacahrro luke quem comprou foi o Vladimir ele comprou para seu filho Davi"
# transformar tudo para minusculo
texto_minusculo = texto_normal.lower()
# quebrar as palavras
texto_qubrado = texto_minusculo.split()
# criar um dict para verificar quantas vezes a mesma letra apareceu
aparicoes = defaultdict(int)

#  este implementa a funcionalidade de quantas vezes aparce um palavra
for palavra in texto_qubrado:

    aparicoes[palavra] += 1

print(aparicoes)


class Conta:
    def __init__(self):
        print("Criando uma conta")


contas = defaultdict(Conta)
contas[15]
contas[15]
