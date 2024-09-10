from math import hypot
ca = float(input("Comprimento do cateto oposto: "))
co = float(input("Comprimento do cateto adiacente: "))
hi = hypot(co, ca)
print(f"A hipotenusa vai medir {hi:.2f}")
