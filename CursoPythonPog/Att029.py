from colorama import Fore
vel = float(input("Qual é a velocidade atual do carro? "))
multa = (vel - 80) * 7
if vel > 80:
    print(Fore.RED + "MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print(Fore.RED + f"voce deve pagar uma multa de " + Fore.YELLOW + f"{multa:.2f}!")
print(Fore.GREEN + "Tenha um bom dia! Dirija com segurança!")
