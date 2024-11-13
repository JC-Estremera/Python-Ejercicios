'''
La idea de este proyecto es crear un programa que evalúe cuan rápido puedes escribir una
oración de manera precisa.
Este programa puede requerir crear una interfaz gráfica de usuario (GUI) mediante el módulo
tkinter. Si eres nuevo en las GUI, este ejemplo es una buena introducción, ya que tan solo
necesitas crear una serie de etiquetas simples, botones y campos de entrada para crear una
ventana. Puedes usar el módulo timeit de Python para manejar el aspecto de temporización
de nuestra prueba de escritura, y el módulo random para seleccionar aleatoriamente una frase
de prueba.
'''

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="¿Veamos cuan rapido eres?").grid(column=0, row=0)
btn = ttk.Button(frm, text="Iniciar", command=root.destroy).grid(column=1, row=0)
root.mainloop()


