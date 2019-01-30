numero = int(input("Dime el numero 1: "))
numero2 = int(input("Dime el numero 2: "))
numero3 = int(input("Dime el numero 3: "))

if numero == numero2 and numero2 == numero3:
	print ("Has escrito tres veces el mismo numero")
elif numero != numero2 and numero != numero3 and numero2 != numero3:
	print ("Los tres numeros que has escrito son distintos")
else:
	print ("Ha escrito uno de los numeros 2 veces")