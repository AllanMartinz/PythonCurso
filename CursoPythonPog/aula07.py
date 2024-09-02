nome = input("Quala seu nome? ")
# o :20 vai preencher o nome em 20 caracteres vai aplicar strings vazias ate completar 20
# dependendo do :=-_<>^ que vc usa vai jogar para direira(<) || esquerda(>) || centralizado(^) || enter a formataçao e a quantidade de caracteres pode preencher com =_-...
print("Prazer em conhecer {:=^20}!".format(nome))

n1 = int(input("Primeiro Numero: "))
n2 = int(input("Segundo Numero: "))
# soma
soma = n1 + n2
# multiplicacao
mult = n1 * n2
# divisao
divi = n1 / n2
# divisao inteira
divin = n1 // n2
# espodenciacao
espo = n1 ** n2
#o end vazio para nao quebrar linha | pode se usar \n no meio da string para quebra a linha
print(f"A soma é {soma}, o produto é {mult} e a divisao {divi:.3f}", end=" ")
print(f"Divisao inteira {divin} e a potencia {espo}")

num = int(input("Digite um numero:"))
ant = num - 1
suc = num + 1
print(f"O antecessor de {num} é {ant} e o sucessor é {suc}")

nota1 = float(input("Digite qual foi a primeira nota: "))
nota2 = float(input("Digie qual foi a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A media do aluno foi {media:.1f}!")

metros = int(input("Digite o valor de metros: "))
cent = metros / 1000
mili = cent / 1000
print(f"Em {metros} há {cent} centimetros ")
print(f"Em {metros} há {mili} milimetros ")

numint = int(input("Digite um numero: "))
tabuada = f"""
1 * {numint} = {numint * 1}
2 * {numint} = {numint * 2}
3 * {numint} = {numint * 3}
4 * {numint} = {numint * 4}
5 * {numint} = {numint * 5}
6 * {numint} = {numint * 6}
7 * {numint} = {numint * 7}
8 * {numint} = {numint * 8}
9 * {numint} = {numint * 9}
10 * {numint} = {numint * 10}
"""
print(f"A tabuada de {numint}! \n {tabuada}")

money = float(input("Quantos reais vc tem? R$"))
dollar = money / 5.61
print(f"Vc pode comprar ate US${dollar}")

largura = float(input("Qual a lagura de sua parede em metros? "))
altura = float(input("Qual a altura de sua parede em metros? "))
areaQuadrada = largura * altura
totalTinta = areaQuadrada / 2**2
print(f"sera usado {totalTinta} litros para pintala ")

preco = float(input("Qual o preco? "))
desconto = preco / 0.05
print(f"com 5% de desconto o preco fica em R$:{desconto}")

salario = float(input("Qual o seu salarios? R$"))
aumento = salario * 0.15
print(f"Com o aumento de 15% agora o seu salario é de {aumento}! ")






