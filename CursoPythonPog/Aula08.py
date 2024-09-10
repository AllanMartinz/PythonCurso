#ao ser importado algo ele ira pegar os itens da biblioteca atibuida
import math
# no math ira importar ceil(arrendodar +), floor(arrendodar -), trunc(eliminar a .), pow(espotenciacao), sqrt(raiz quadrada), factorial(fatoracao)
#from math import sprt, ceil
#caso queira importar um item especifico | nao sera necesario invocar o math | para add + devera usar a ,
import random
#importatar as bibliotecas random
num = int(input("Digite o numero para ser calculado: "))
raiz = math.sqrt(num)
print(f"A raiz de {num} é igual a {math.ceil(raiz)}!")

#ira randomizar um numero inteiro aleatorio entre 1 - 6
dado = random.randint(1,6)
print(f"vc tirou um {dado}")

#caso queira ver a biblioteca https://docs.python.org/3/

numReal = float(input("Digite um numero: "))
print(f"O numero {numReal} tem a parte inteira {math.trunc(numReal)}")

























#! tem que ver se tem no C# \ nao se perda