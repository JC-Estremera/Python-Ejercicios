'''
La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible
en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de
herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de
instalación de pip).
Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
luego manejar la conversión de texto a voz.
'''
import newspaper
import gtts
import nltk

# Inicializacion de Variables
texto = ""
idiomas = gtts.tts.tts_langs()

# Peticion del Articulo que vamos a convertir a Voz 
while True:
    url = input("Introduzca una url: ")

    # Descargar y asignar el texto a convertir segun la url
    try:
        articulo = newspaper.Article(url)
        articulo.download()
        articulo.parse()
        texto = articulo.text
        break
    except:
        print("Url no válida")

# Transformar el texto en palabras unicas para saber el idioma del Articulo
# Dividimos el texto de entrada en tokens o palabras unicas
tokens = nltk.tokenize.word_tokenize(texto)
# Las Palabras han de estar en minusculas para la Comparacion posterior
tokens = [token.strip().lower() for token in tokens]

# Creamos un dict donde almacenaremos la cuenta de las stopwords para cada idioma
lang_count = {}
# Por cada idioma
for lang in idiomas:
    # Obtenemos las palabras clave del idioma del módulo nltk
    try:
        stop_words = nltk.corpus.stopwords.words(idiomas[lang].lower())
    except OSError:
        stop_words = []
    # Inicializa a 0 el contador para cada idioma
    lang_count[lang] = 0 

    # Recorremos las palabras del texto a analizar
    for word in tokens:
        if word in stop_words: # Si la palabra se encuentra entre las stopwords, incrementa el contador
            lang_count[lang] += 1

# Obtiene el idioma con el número mayor de coincidencias
idioma_detectado = max(lang_count, key=lang_count.get)

# Transformamos el texto en voz y lo guardamos
tts = gtts.gTTS(texto, lang=idioma_detectado)
try:
    tts.save("Texto.mp3")
except:
    print("ERROR")
