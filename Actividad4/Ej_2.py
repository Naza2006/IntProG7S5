#Detectar si el suario esta inactivo por mas de 30 dias

import datetime as dt

fecha_inicio_sesion = input("Ultimo inicio de sesion en formato YYYY-MM-DD: ")
fecha_inicio_sesion = datetime.datetime.strftime(fecha_inicio_sesion, "%Y-%m-%d")

fecha_actual = dt.datetime.now

print(fecha_inicio_sesion, fecha_actual)

contra_dias = (fecha_inicio_sesion - fecha_actual)
if contra_dias > 30:
    print("Inactivo por mas de 30 dias")
    
else:
    print("Estamos bien.")