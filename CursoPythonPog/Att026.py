frase = str(input("Digite a frase: ")).strip().upper()
print(f"A letra A aparece {frase.count("A")} vezes na frase")
print(f"A primeira letra A apareceu na posicao {frase.find("A")+1}")
print(f"A ultima letra A aparareceu na posição {frase.rfind("A")+1}")