from lxml import etree
doc = etree.parse('sevilla.xml')

def latylong(doc):
	latitud = doc.xpath('//latitud/text()')[0]
	longitud = doc.xpath('//longitud/text()')[0]
	return latitud,longitud

latitud,longitud = latylong(doc)

print ("Latitud:",latitud)
print ("Longitud:",longitud)