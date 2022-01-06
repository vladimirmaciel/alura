# iremos utilizar o counter
from collections import defaultdict, Counter

texto_normal = "Bem vindo meu nome é vladimir , meu filho é Davi , minha esposa Amanda e meu cacahrro luke quem comprou foi o Vladimir ele comprou para seu filho Davi"
# transformar tudo para minusculo
texto_minusculo = texto_normal.lower()
# quebrar as palavras
texto_qubrado = texto_minusculo.split()
# criar um dict para verificar quantas vezes a mesma letra apareceu
aparicoes = Counter(texto_qubrado)
print(aparicoes)
