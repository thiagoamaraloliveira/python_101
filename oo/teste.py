def cria_conta(numero, titular, saldo, limite):
    conta = {"numero":numero, "titular":titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor
    print()

def saca(conta, valor):
    conta["saldo"] -= valor
    print()

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))