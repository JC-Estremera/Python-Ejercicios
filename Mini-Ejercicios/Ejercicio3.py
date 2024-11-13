'''
Encuentra o crea algunos textos que te gustaría analizar (puedes visitar
Project Gutenberg (http://gutenberg.org/) o crear textos usando ChatGPT).
Copia el texto sin formato desde tu navegador en un archivo de texto en tu
computadora (o descarga los archivos). Averigua cuántas veces aparece una
palabra o frase en el texto (puedes usar el método count()).
'''

file_name = "Anne1.txt"

try:
    with open(file_name) as file:
        contenido = file.read()
    palabra = input("Introduce la palabra que quieres contar: ")
    count = contenido.count(palabra)
    print(f"El numero de veces que aparece la palabra {palabra} es de:", count)
except FileNotFoundError:
    print(f"No existe el archivo {file_name}")