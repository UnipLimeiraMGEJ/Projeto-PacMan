import random  # Importa a biblioteca random

def jogar():  # Função jogo_forca

    abertura()  # Chama a função abertura
    palavra_secreta = palavra_aleatoria()  # Chama a função palavra_secreta
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta) # Lista que adiciona um _ na lista de letras acertadas baseado no tamanho da palavra secreta

    enforcou = False  # Variável que diz se o jogador foi enforcado
    acertou = False  # Variável que diz se o jogador acertou a palavra secreta
    erros = 0  # Variável que conta os erros
    
    print(letras_acertadas)  # Imprime na tela a prévia de quantas letras tem a palavra secreta

    # Enquanto o jogador não for enforcado e não acertar a palavra secreta
    while (not enforcou and not acertou):

        # Pede para o jogador digitar uma letra
        # Pede para o jogador digitar uma letra
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()  # Remove os espaços em branco e deixa tudo em maiúsculo
        
        if(chute in palavra_secreta): # Se a letra digitada estiver na palavra secreta
            index = 0  # Variável que vai guardar o índice da letra
            for letra in palavra_secreta:  # Para cada letra na palavra secreta
                # Se o chute for igual a letra
                if (chute == letra): # Imprime na tela caso o chute seja igual a letra
                    letras_acertadas[index] = letra # Coloca a letra na lista de letras acertadas
                index += 1  # Incrementa o índice
        else:
            erros += 1  # Incrementa o número de erros
            
        enforcou = erros == 6  # Se o número de erros for igual a 6, o jogador é enforcado
        acertou = "_" not in letras_acertadas  # Se não tiver mais "_" na lista de letras acertadas, o jogador acertou a palavra secreta
        print(letras_acertadas)  # Imprime na tela a lista de letras acertadas

    # Isso aqui é indicar que acabou o jogo
    if(acertou):
        print("Você ganhou!") 
    else:
        print("Você perdeu!") 
    print("Fim do jogo")  











# Apartir daqui são só as funções 










        # Isso aqui é só pra deixar o output mais bonito
def abertura():  # Função de imprimir a abertura
    print("*********************************") 
    print("***Bem vindo ao jogo de Forca!***")  # Imprime na tela
    print("*********************************")

    # Isso aqui é pra chamar a palavra secreta
def palavra_aleatoria():  # Chama a função palavra_aleatoria
    palavra_secreta = "paralelepipedo".upper()  # Palavra secreta
    return palavra_secreta  # Retorna a palavra secreta
    # Esse código todo era pra fazer parte da função de cima e chamar uma palavra aleatória de um arquivo .txt, mas não funciona
#              arquivo = open("palavras.txt", "r")  # Abre o arquivo
#              palavras = []  # Cria uma lista vazia
#             
#              for linha in arquivo:  # Para cada linha no arquivo
#                    linha = linha.strip()  # Remove os espaços em branco
#                    palavras.append(linha)  # Adiciona a linha na lista
#                 
#              arquivo.close()  # Fecha o arquivo
#               
#              numero = random.randrange(0, len(palavras))  # Gera um número aleatório
#              palavra_secreta = palavras[numero].upper()  # Pega a palavra secreta

def inicializa_letras_acertadas(palavra):  # Função que inicializa as letras acertadas
    return ["_" for letra in palavra]  # Retorna uma lista com "_" para cada letra da palavra secreta
























if (__name__ == "__main__"):  # Se o arquivo for executado diretamente
    jogar()  # Executa a função de jogar

