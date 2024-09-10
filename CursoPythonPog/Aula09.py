frase = "Curso em Video Python"
print(frase)# --> Curso em Video Android
print(frase[3])# --> s
print(frase[3:13])# -->  so em Vide
print(frase[:13])# -->  Curso em Vi
print(frase[13:])# -->  o Python
print(frase[1:15])# -->  urso em Video Python
print(frase[1:15:2])# -->  us mVdo
print(frase[1::2])# -->  us mVdoPto
print(frase[::2])# -->  Croe ie yhn
#para python a maioria das coisas sao objs
print(frase.count("o"))# --> 3
print(frase.count("O"))# --> 0
print(frase.upper().count("O"))# --> 3
frase2 = "      Curso em Video Python       "
print(len(frase2))# --> 34
print(len(frase2.strip()))# --> 21
print(frase.replace("Python", "Android"))# --> Curso em Video Android
print("Curso" in frase)# --> True
print(frase.find("Video"))# --> 9
print(frase.lower().find("video"))# --> 9
print(frase.find("poggers"))# --> -1
print(frase.split())# --> dividir - ['Curso', 'em', 'Video', 'Python'] transforma em uma lista


#para imprimir um txto inteiro precisa """ """
print("""muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa
muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa
muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa
muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa - muita coisa""")