'''
Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los
jugadores.También puedes definir una serie de asignaciones de teclas para establecer los
controles del usuario para las paletas de los jugadores izquierda y derecha.
'''

import turtle
from turtle import *

Screen().setup(1920, 1080, 960, 540)
title("Juego Pong")
hideturtle()



penup()
goto((0,100))
pendown()
pensize(2)
fillcolor("blue")
begin_fill()
circle(20)
end_fill()

Screen().mainloop()