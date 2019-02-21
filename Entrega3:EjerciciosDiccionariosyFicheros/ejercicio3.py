from crypt import crypt
crypt('asdasd','$6$7jszq4YU$')


with open("passwd.txt","r") as fichero:
	contras = fichero.readlines()
	for linea in contras:
		contras = linea.split("\n")
		print (contras)

with open("ficheroshadow.txt","r") as fichero2:
	shadow = fichero2.readlines()
	for linea2 in shadow:
		shadow = linea2.split(":")

