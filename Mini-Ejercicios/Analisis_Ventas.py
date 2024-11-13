'''
Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los
últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor
venta.
Pista 1: Puedes crear dos listas, una con las ventas por cada día del mes como por ejemplo…
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
Y otra lista con los días de la semana:
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", „Domingo“]
Después puedes crear una nueva lista con una entrada por cada día de la semana y usar un bucle
para añadir a esta lista la suma de las ventas correspondientes a cada uno de los días de la
semana.
Pista 2: Puede que necesites una variable que lleve la cuenta del día de la semana actual y se
reinicie a cero cuando llegue al séptimo día. 
'''

# Definimos variables
dias_semana = [["Lunes", 0], ["Martes", 0], ["Miércoles", 0], ["Jueves", 0], ["Viernes", 0], ["Sábado", 0], ["Domingo", 0]]
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]

dia = 0
# Bucle que recorre cada dia del mes y suma el total segun 
for venta_dia in ventas:
    dias_semana[dia][1] = dias_semana[dia][1] + venta_dia
    if dia == 6:
        dia = 0
    else:
        dia += 1

# Imprimimos por pantalla la facturacion
for dia in dias_semana:
    print(f"El {dia[0]} se ha facturado {dia[1]}")