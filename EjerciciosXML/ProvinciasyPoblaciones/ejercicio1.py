def nombreprovincias(doc):
	lista = doc.xpath("//nombre/text()")
	return lista

from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

for provincia in nombreprovincias(doc):
	print (provincia)