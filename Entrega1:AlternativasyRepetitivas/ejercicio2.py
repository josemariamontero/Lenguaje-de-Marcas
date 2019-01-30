anio_actual = int(input("Dime el año actual en el que nos encontramos: "))
anio_aleatorio = int(input("Dime un año cualquiera: "))

if anio_actual - anio_aleatorio == 1 or anio_aleatorio - anio_actual == 1:
	print ("La diferencia es exactamente de un año")
elif anio_actual < anio_aleatorio:
	print ("Para llegar al año",anio_aleatorio,"faltan",anio_aleatorio - anio_actual,"años")
elif anio_actual > anio_aleatorio:
	print ("Desde el año",anio_aleatorio,"han pasado",anio_actual - anio_aleatorio,"años")
elif anio_actual == anio_aleatorio:
	print ("Son el mismo año")
