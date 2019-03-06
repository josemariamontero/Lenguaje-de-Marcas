from lxml import etree
doc = etree.parse('sevilla.xml')

def vientotemphum(doc):
	viento = doc.xpath('//condiciones_actuales/viento/text()')[0]
	temperatura = doc.xpath('//condiciones_actuales/temperatura/text()')[0]
	humedad = doc.xpath('//condiciones_actuales/humedad/text()')[0]
	return viento,temperatura,humedad

viento,temp,humedad = vientotemphum(doc)

print ("Viento:",viento)
print ("Temperatura:",temp)
print ("Humedad:",humedad)