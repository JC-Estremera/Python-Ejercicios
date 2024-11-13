'''
Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y
en que posición. Puedes usar find()).
Puedes usar el archivo pi_10000.txt
'''

file_name = "pi_10000.txt"

try:
    with open(file_name) as file:
        contenido = file.read()
    fecha = input("Escribe tu fecha de nacimiento sin signos de separacion: ")
    find = contenido.find(fecha)
    print("La fecha se encuentra en la posicion", find)
except FileNotFoundError:
    print(f"No existe el archivo {file_name}")