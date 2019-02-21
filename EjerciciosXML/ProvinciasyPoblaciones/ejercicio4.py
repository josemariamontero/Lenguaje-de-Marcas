def provincias(nombre,doc):
	poblaciones = doc.xpath('//provincia[nombre="%s"]/localidades/localidad/text()' % nombre)
	return poblaciones

from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

nombre = input("Dime una provincia: ")

for i in provincias(nombre,doc):
	print (i)

