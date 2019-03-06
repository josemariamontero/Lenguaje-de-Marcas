from lxml import etree
doc = etree.parse('users.xml')

def busqueda(cadena,doc):
	nombre = doc.xpath("//user[starts-with(firstname='%s')]/firstname/text()" % cadena)
	apellidos = doc.xpath("//user/lastname/text()")
	for i in range(len(nombre)):
		nombre[i] = nombre[i] + " " + apellidos[i]
	return nombre

nombre = input("Introduce el nombre de un usuario: ")

print (busqueda(nombre,doc))