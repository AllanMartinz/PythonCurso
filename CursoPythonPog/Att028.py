from random import randint
from colorama import Fore
print(Fore.YELLOW + "-=-" * 20)
print(Fore.BLUE + "vou pensar em um numero entre 0 - 5. tente adivinhar...")
print(Fore.YELLOW + "-=-" * 20)
num = int(input(Fore.RESET + "Em que numero eu pensei? "))
print(Fore.MAGENTA + "POCESSANDO...")
numPen = randint(0, 5)
if num == numPen:
    print(Fore.GREEN + f"EU PERDI! eu pensei no numero {numPen}")
else:
    print(Fore.RED + f"GANHEI! eu pensei no numero {numPen} e nao no {num}")