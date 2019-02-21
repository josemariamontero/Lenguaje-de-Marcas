def ciudadesgrandes(localidad,doc):
	localidad = doc.xpath('//provincia[nombre="%s"]//localidad[@c="1"]/text()' % nombre)
	return localidad

from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

nombre = input("Dime una provincia: ")

for i in ciudadesgrandes(nombre,doc):
	print (i)