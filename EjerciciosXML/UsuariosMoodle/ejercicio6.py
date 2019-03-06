from lxml import etree
doc = etree.parse('users.xml')

def ultimo_acceso(doc):
	lista = []
	acceso = sorted(list(doc.xpath('//user/lastacces/text()')),reverse=True)
	for i in acceso:
		nombre = doc.xpath('//user[lastaccess="%s"]/firstname/text()' % i)
		apellido = doc.xpath('//user[lastaccess="%s"]/lastname/text()' % i)
		lista.append(nombre)
	return lista

	print(ultimo_acceso(doc))