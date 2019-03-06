from lxml import etree
doc = etree.parse('users.xml')

def listado_localidad(doc):
	usuarios = {}
	localidades = doc.xpath('//user/city/text()')
	for i in localidades:
		nombres = doc.xpath('//user[city="%s"]/firstname/text()' % i)
		apellidos = doc.xpath('//user[city="%s"]/lastname/text()' % i)
		usuarios[i] = []
		for i in range(len(nombres)):
			usuarios[i].append(nombres[i] + " " + apellidos[i])
	return usuarios

print (listado_localidad(doc))