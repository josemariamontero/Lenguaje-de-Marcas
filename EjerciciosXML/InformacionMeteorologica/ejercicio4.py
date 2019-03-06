from lxml import etree
doc = etree.parse('sevilla.xml')

def busquedapronostico(fecha,hora,doc):
	fecha = doc.xpath('//pronostico_horas/hora/@fecha')
	hora = doc.xpath('//pronostico_horas/hora/@id')
	for hora,fecha in zip(hora,fecha):
		temperatura = doc.xpath('//pronostico_horas/hora[@id="%s" and @fecha="%s"]/temperatura/text()' % (hora,fecha))[0]
		viento = doc.xpath('//pronostico_horas/hora[@id="%s" and @fecha="%s"]/viento/text()' % (hora,fecha))[0]
		precipitacion = doc.xpath('//pronostico_horas/hora[@id="%s" and @fecha="%s"]/precipitacion/text()' % (hora,fecha))[0]
		humedad = doc.xpath('//pronostico_horas/hora[@id="%s" and @fecha="%s"]/humedad/text()' % (hora,fecha))[0]
		return temperatura,viento,precipitacion,humedad
	return None

temp,viento,preci,humedad = busquedapronostico("2016-02-28","07:00:00",doc)

print ("Temperatura:",temp)
print ("Viento:",viento)
print ("Precipitacion:",preci)
print ("Humedad:",humedad)