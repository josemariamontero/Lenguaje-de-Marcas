numero = int(input("Dime el numero 1: "))
numero2 = int(input("Dime el numero 2: "))

while numero2 == 0:
	print ("No se puede dividir entre 0")
	numero2 = int(input("Dime el numero 2: "))

if numero % numero2 == 0:
	print("La división es exacta.", "Cociente:",numero//numero2)
else:
	print("La division no es exacta.", "Cociente:",numero//numero2, "Resto:",numero % numero2)