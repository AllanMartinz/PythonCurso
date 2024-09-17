dis = float(input("qual e  a distancia da sua viagem? "))
print(f"Voce esta prestes a cpmeçar uma viagem de {dis}Km.")
if dis >= 200:
    print(f"E o preco da sua passagem sera de R${dis * 0.45:.2f}")
else:
    print(f"E o preco da sua passagem sera de R${dis * 0.50:.2f}")