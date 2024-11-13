'''
El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se
compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
catalán la ”Ç”, en alemán la ”ß”, etc.).
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual. 
'''

alfabeto1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
alfabeto2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
frase = input("Escribe la frase a encriptar: ")
frase_encriptada = []
frase_comparar = input("Escribe la frase encriptada: ")

for letra in frase:
    i = 0
    if letra.isupper():
        up = True
    else:
        up = False
    letra = letra.lower()
    if letra in alfabeto1:
        for letter in alfabeto1:
            if letter == letra:
                break
            i = i + 1
        if up:
            frase_encriptada.append(alfabeto2[i].upper())
        else:
            frase_encriptada.append(alfabeto2[i])
    elif letra in alfabeto2:
        for letter in alfabeto2:
            if letter == letra:
                break
            i = i + 1
        if up:
            frase_encriptada.append(alfabeto1[i].upper())
        else:
            frase_encriptada.append(alfabeto1[i])
    else:
        frase_encriptada.append(letra)

for letra in frase_encriptada:
    print(letra, end = "")
print()

if frase_encriptada == frase_comparar:
    print("La frase esta encriptada")
else:
    print("La frase no esta encriptada")