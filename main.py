import random
import os

base1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

if os.name == 'nt': 
    os.system('cls' )
else:
    os.system('clear')

try:
    opt = int(input("Ingrese la cantidad de codigos que desea generar: "))
    if opt <= 0:
        print("ingresa un numero mayor que cero.")
    else:
        with open("codes.txt", "w") as file:
            for _ in range(opt):
                rnd = "discord.gift/" + "".join(random.choices(base1, k=10))
                print(rnd)
                file.write(rnd + "\n")
        print(f"Se han generado {opt} codigos y se han guardado en 'codes.txt'.")
except ValueError:
    print("ingresa un número válido.")
