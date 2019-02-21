def nombrepoblaciones(doc):
	lista = doc.xpath("//localidad/text()")
	return lista

from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

for localidad in nombrepoblaciones(doc):
	print (localidad)