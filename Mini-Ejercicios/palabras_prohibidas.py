palabras_aleatorias = ["casa", "perro", "gato", "libro", "raton"]
letras_prohibidas = ["a", "u"]
lista_filtrada = []

for palabra in palabras_aleatorias:
    incluir = True
    for letra_prohibida in letras_prohibidas:
        if letra_prohibida in palabra:
            incluir = False
    if incluir:
        lista_filtrada.append(palabra)

print("Lista original: ", palabras_aleatorias)
print("Letras prohibidas: ", letras_prohibidas)
print("Lista filtrada: ", lista_filtrada)