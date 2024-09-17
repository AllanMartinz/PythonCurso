print("-=-" * 20)
print("Analisador de Trinagulos")
print("-=-" * 20)
r1 = float(int("Primeiro segmento: "))
r2 = float(int("Segundo segmento: "))
r3 = float(int("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print("Os segmentos acima PODEM FORMAR triangulo!")
else:
    print("Os segmentos acima NAO PODEM FORMAR triangulo!")
