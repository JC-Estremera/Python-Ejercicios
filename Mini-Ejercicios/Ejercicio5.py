'''
Escribe un programa que solicite al usuario su número favorito. Utiliza
json.dump() para almacenar este número en un archivo. Escribe un
programa separado que lea este valor e imprima el mensaje: "Sé cuál es tu
número favorito… Es ____.” Combina ambos programas en un solo archivo
(puedes crear tantas funciones como necesites). Si el número ya está
almacenado, muestra el número favorito al usuario. Si no lo está, solicita al
usuario su número favorito y guárdalo en un archivo. Ejecuta el programa al
menos dos veces para asegurarte de que funciona correctamente.
'''

import json

numero = int(input("Escribe tu numero favorito: "))

try:
    with open("numero_favorito.json", "w") as file:
        json.dump(numero, file)
except FileNotFoundError:
    print("El Archivo no existe.")
try:
    with open("numero_favorito.json") as file:
        numero = file.read()
        print("Tu numero favorito es:", numero)
except FileNotFoundError:
    print("El Archivo no existe.")