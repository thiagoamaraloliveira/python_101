import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.randrange(1, 101))
total_de_tentativas = 0

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível:"))

if (nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

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