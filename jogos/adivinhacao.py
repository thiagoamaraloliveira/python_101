print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))

    chute_str = input("Digite um número entre 1 a 100:")
    print("Você digitou ",chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 a 100")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou! o seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! o seu chute foi menor do que o número secreto.")


print("Fim de Jogo!!")
print("**************")