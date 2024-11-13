'''
La idea de este proyecto es crear un programa que pruebe la conectividad de sitios web.
Puedes usar los modulos urllib y tkinter para crear una interfaz gráfica de usuario (GUI) que
permita a los usuarios ingresar una dirección web. Después de haber recopilado la dirección
web del usuario, puedes pasarla a una función para devolver un código de estado HTTP para
el sitio web actual mediante la función .getcode() del módulo urllib.
En este ejemplo, simplemente determinamos si el código HTTP es 200. Si lo es, sabemos que
el sitio está funcionando; de lo contrario, informamos al usuario de que no está disponible.
'''