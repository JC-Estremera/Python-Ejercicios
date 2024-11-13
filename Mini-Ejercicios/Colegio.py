'''
Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
completo.
'''

# Cada Estudiante tiene un Nombre, Nota_Deberes, Nota_Examenes, Nota_Proyecto
lista_estudiantes = [["Sergio", 6, 7, 6], ["Luis", 5, 7, 3]]
lista_medias = []

for estudiante in lista_estudiantes:
    suma = sum(estudiante[1:3]) / 3
    lista_medias.append(suma)
    print(f"La nota media de {estudiante[0]} es {suma :.2f}")

print(f"La nota media de la clase es {sum(lista_medias) / len(lista_medias) :.2f}")
