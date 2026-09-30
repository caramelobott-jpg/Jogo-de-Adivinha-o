import random

numero_secreto = random.randint(1, 100)


while True:
    palpite = int(input("Digite seu numero:"))
    if palpite == (numero_secreto):
        print("Vencendor")
        break
    elif palpite < numero_secreto:
        print("Tente um numero maior")

    else:
        print("Tente um numero menor")
