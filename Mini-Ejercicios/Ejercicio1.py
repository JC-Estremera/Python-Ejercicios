'''
Un problema común al solicitar una entrada numérica ocurre cuando las
personas ingresan texto en lugar de números. Cuando intentas convertir la
entrada a un entero (int), obtendrás un ValueError. Escribe un programa que
solicite dos números. Suma los números y muestra el resultado. Captura el
ValueError si alguno de los valores de entrada no es un número e imprime un
mensaje de error amigable. Prueba tu programa ingresando dos números y
luego ingresando texto en lugar de un número. Envuelve tu código del en un
bucle while para que el usuario pueda continuar ingresando números incluso
si comete un error ingresando texto en lugar de un número.
'''

numero1 = 0
numero2 = 0
salida = ""

while True:
    try:
        numero1 = int(input("Introduce el primer numero: "))
        numero2 = int(input("Introduce el segundo numero: "))
    except ValueError:
        print("Ha introducido una entrada de datos equivocada. \nIntentelo de nuevo.")
        continue
    print("La suma es:", numero1 + numero2)
    salida = input("Introduce s para poder continuar, en cualquier otro caso pulse cualquier letra: ")
    if salida.lower() == "s":
        break