print("\033[7;30;44mOlà Mundo!\033[m")
a = 3
b = 5
print(f"Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m")
nome = "Guanabara"
print(f"Ola! {"\033[4;36m"}{nome}{"\033[m"}")
cores = {"limpa" : "\033[m","azul" : "\033[34m", "amarelo" : "\033[33m", "pretobranco" : "\033[7;30m"}
print(f"{cores["azul"]}Hello World!{cores["limpa"]}")

