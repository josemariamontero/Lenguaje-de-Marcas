from crypt import crypt
from getpass import getpass
crypt('asdasd','$6$7jszq4YU$')

with open("ficheroshadow.txt","r") as fichero:
	lineas = fichero.readlines()
	usuario = input("Dime el nombre de usuario: ")
	for i in lineas:
		if usuario == i.split(":")[0]:
			contra	= getpass("Dime la contraseña del usuario: ")
			sal = i.split(":")[1][:12]
			if crypt(contra,sal) == i.split(":")[1]:
				print ("Usuario Correcto")
			else:
				print ("Usuario Incorrecto")			



