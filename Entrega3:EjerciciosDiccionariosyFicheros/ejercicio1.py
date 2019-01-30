def calcula_dc(lista):
	pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
	aux = []
	for i in range(10):
		aux.append(lista[i]*pesos[i])
	resto = 11 - sum(aux) %11
	if resto == 10:
		return 1
	elif resto == 11:
		return 0
	else:
		return resto

numero_cuenta = input("Introduce el numero de cuenta: ")

if len(numero_cuenta) != 20:
	print ("Numero de cuenta incorrecto")
	numero_cuenta = input("Introduce el numero de cuenta: ")

lista = list(numero_cuenta)

lista_codigo1 = ['0','0'] + lista[:8]
lista_codigo2 = lista[10:]

codigo1 = calcula_dc(list(map(int,lista_codigo1)))
codigo2 = calcula_dc(list(map(int,lista_codigo2)))

if codigo1 == int(lista[8]) and codigo2 == int(lista[9]):
	print ("Correcto")
else :
	print ("Incorrecto")

with open("bancos.txt","r") as fichero:
	for linea in fichero:
		if numero_cuenta[:4] == linea[:4]:
			print ("Entidad Bancaria:",linea[6:])
		

#08706873579988768277