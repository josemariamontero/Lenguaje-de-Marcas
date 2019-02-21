def ciudadesgrandes(localidad,doc):
	localidad = doc.xpath('//localidades/localidad[text()="%s" and @c="1"]/text()' % nombre)
	if len(localidad) > 0:
		return doc.xpath('//localidades[localidad="%s"]/../nombre/text()' % nombre)[0]
	else:
		return None

from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

nombre = input("Dime una provincia: ")

for i in ciudadesgrandes(nombre,doc):
	print (i)