numero = int(input("Dime un numero: "))

while numero < 0:
	print("Escribe un numero mayor que 0")
	numero = int(input("Dime un numero: "))

print("Los divisores de",numero,"son: ",end="")

for i in range(1,numero + 1):
	if numero % i == 0:
		print (i,end=" ")
print()
