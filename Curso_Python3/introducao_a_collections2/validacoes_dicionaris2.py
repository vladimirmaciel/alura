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
    # contador_temp = aparicoes.get(
    #     palavra, 0
    # )
    #  aparicoes modificou devido a funcao defalutdict()
    contador_temp = aparicoes[palavra]
    # utilizacao da funcao get para verficar se exit a palavra caso contrario retorna 0
    aparicoes[palavra] = contador_temp + 1

print(aparicoes)
