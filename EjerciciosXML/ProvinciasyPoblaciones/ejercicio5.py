def poblaciones(nombre,doc):
	poblacion = doc.xpath('//localidades[localidad="%s"]/../nombre/text()' % nombre)
	return poblacion

from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

nombre = input("Dime una localidad: ")

for i in poblaciones(nombre,doc):
	print (i)