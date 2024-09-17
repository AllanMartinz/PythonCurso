from colorama import Fore
num = int(input(Fore.MAGENTA + "Me diga um numero qualquer: "))
if num % 2 == 0:
    print(Fore.RESET + f"O numero {num} é {Fore.BLUE + "PAR"}")
else:
    print(Fore.RESET + f"O numero {num} é {Fore.BLUE + "IMPAR"}")