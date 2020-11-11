import random

listTrue = ["sim", "Sim", "SIM", "S", "s"]
listFalse = ["nao", "não", "Nao", "Não", "NÃO", "NAO", "n", "N", "ñ", "Ñ"]

def dice():
    res = random.randrange(1, 7)
    return res

def ini():
    start = input('Gostaria de jogar o dado? sim/nao')

#condição para repetição
    while start in listTrue:
        print('Resultado:', str(dice()))
        start = input("Gostaria de jogar novamente? sim/nao")

    if start in listFalse:
        print('Ok, finalizando')

    else:
        print('Não entendi...')
        ini()
ini()
