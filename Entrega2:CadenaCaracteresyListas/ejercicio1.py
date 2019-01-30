cadena = str(input("Introduce una cadena de caracteres: "))
cadena2 = str(input("Introduce otra cadena de caracteres: "))

if cadena2.upper() in cadena.upper():
	print ("La segunda cadena es una subcadena de la primera")
else:
	print ("La segunda cadena no es una subcadena de la primera")