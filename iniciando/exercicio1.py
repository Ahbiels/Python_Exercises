import os

os.system("clear")
altura_cm = input("Digite sua altura em centimetros: ")
peso_kg = input("Digite seu peso em kg: ")

os.system("clear")

IMC = int(peso_kg) / int(altura_cm)**2 * 10000 
print(f"IMC Atual: {round(IMC,2)}")

if IMC < 18.5:
    print("Voce está magro demais")
elif IMC >= 18.5 and IMC < 24.9:
    print("Voce está dentro do peso")
elif IMC >= 24.9 and IMC < 29.9:
    print("Voce está acima do peso")
elif IMC >= 29.9 and IMC < 39.9:
    print("Voce está obeso")
elif IMC >=39.9:
    print("Voce está muito acima do peso")