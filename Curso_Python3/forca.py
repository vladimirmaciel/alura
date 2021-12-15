import random


def msg_abertura():

    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')


def carrega_palavras_secretas():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()  # função strip limpa espaço em branco e tira o \n
        palavras.append(linha)

    arquivo.close()

    # np é o número da posição na lista que vai ser escolhido aletoriamente
    np = random.randrange(0, len(palavras))

    print(palavras, np)

    palavra_secreta = palavras[np].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):

    return ["_" for letras_acertadas in palavra]


def pede_chute():
    chute = input("Qual letra ? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):

            # Opcao 1 de modificar
            # letras_acertadas[index] = letra

            # opcao 2 utilizando pop e insert
            letras_acertadas.pop(index)
            letras_acertadas.insert(index, letra)

        index += 1


def imprime_msg_vencedor():

    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_msg_perdedor(palavra_secreta):
    print("Você perdeu !!")
    print(f"A palvra secreta era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    msg_abertura()
    palavra_secreta = carrega_palavras_secretas()

    # código abaixo vai mostrar quantidade traço de acordo com a palavra
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas, "\n")

    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print(f"\nOps, você errou! Faltam {6-erros} tentativas.")
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas, "\n")

    if(acertou):
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor(palavra_secreta)


if(__name__ == '__main__'):
    jogar()
