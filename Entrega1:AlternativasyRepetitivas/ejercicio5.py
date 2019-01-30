cantidad = int(input("Dime cuantos numeros vas ha introducir: "))

while cantidad <= 0:
	print ("Imposible")
	cantidad = int(input("Dime cuantos numeros vas ha introducir: "))

numero = int(input("Dime un numero: "))
for i in range(cantidad - 1):
	numero2 = int(input("Dime un numero mas grande que %d: "%numero))
	if numero2 < numero:
		print (numero2,"no es mayor que",numero)
		numero2 = int(input("Dime un numero mas grande que %d: "%numero))
