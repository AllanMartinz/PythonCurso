nome = str (input("Qual seu nome? "))
if nome == "Gustavo":
    print("Que nome lindo vc tem!")
else:
    print("Credo!!!")
print(f"Bom dia {nome}!")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
if m >= 70.0:
    print("Vc foi aprovado!!")
else:
    print("vc foi reprovado!!")
print(f"A sua media é {m}")

