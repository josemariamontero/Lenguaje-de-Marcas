from lxml import etree
doc = etree.parse('users.xml')

def cambioavatar(doc):
	nombres = doc.xpath("//user[picture=1]/firstname/text()")
	apellidos = doc.xpath("//user[picture=1]/lastname/text()")
	for i in range(len(nombres)):
				nombres[i] = nombres[i] + " " + apellidos[i]
	return nombres

print(cambioavatar(doc))