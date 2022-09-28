import random # Importa a biblioteca random

# Isso aqui é só pra deixar o output mais bonito
print("--------------------------------") #
print("Bem vindo ao jogo de adivinhação") # Imprime na tela
print("--------------------------------") #

# Isso aqui é pra definir o número secreto
numero_secreto = round(random.random() * 100) # random.random() gera um número aleatório entre 0 e 1
total_de_tentativas = 3 # Define o número de tentativas


# Isso aqui é pra definir o nível de dificuldade
for rodada in range(1, total_de_tentativas + 1): # range(1, 4) = 1, 2, 3
    print("Tentativa {} de {}".format(rodada, total_de_tentativas)) # Imprime na tela
    chute = input("Digite um número entre 1 e 100: ") # Imprime na tela e recebe um valor
    print("Você digitou ", chute) # Imprime na tela
    chute = int(chute) # Converte o valor recebido para inteiro
    
    # Isso aqui é pra verificar se o chute está correto
    if(chute < 1 or chute > 100): # Verifica se o valor está entre 1 e 100
        print("Você deve digitar um número entre 1 e 100!") # Imprime na tela
        continue # Volta para o início do loop

    acertou = chute == numero_secreto # Verifica se o valor é igual ao número secreto
    maior = chute > numero_secreto # Verifica se o valor é maior que o número secreto
    menor = chute < numero_secreto # Verifica se o valor é menor que o número secreto

# Isso aqui é pra imprimir o resultado
    if (acertou): # Verifica se o valor é igual ao número secreto
        print("Você acertou!") # Imprime na tela
        break # Sai do loop
    else: # Se o valor não for igual ao número secreto
        if (maior): # Verifica se o valor é maior que o número secreto
            print("Você errou! O seu chute foi maior que o número secreto.") # Imprime na tela
        elif (menor): # Verifica se o valor é menor que o número secreto
            print("Você errou! O seu chute foi menor que o número secreto.") # Imprime na tela
    
# Isso aqui é indicar que acabou o jogo
print("Fim do jogo") # Imprime na tela