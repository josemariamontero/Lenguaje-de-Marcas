from random import randint
cantidad = int(input("Numero de preguntas: "))
contador_bien = 0
contador_mal = 0

while cantidad <= 0:
	print ("El numero de preguntas debe ser al menos 1")
	cantidad = int(input("Numero de preguntas: "))

for i in range(cantidad):
	numero = randint(2,10)
	numero2 = randint(2,10)
	aleatorio = int(input("¿Cuanto es %d * %d? " % (numero, numero2)))

	if numero * numero2 == aleatorio:
		print ("Correcto")
		contador_bien = contador_bien + 1
	else:
		print ("Incorrecto")
		contador_mal = contador_mal + 1

print ("Ha contestado bien", contador_bien, "preguntas")
print ("Ha contestado mal", contador_mal, "preguntas")
nota = (contador_bien / cantidad) * 10
print ("Le corresponde una nota de %.2f"%nota)