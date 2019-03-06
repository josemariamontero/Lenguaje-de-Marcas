from lxml import etree
doc = etree.parse('users.xml')

def usuariosyprofes(doc):
	nombres = doc.xpath("//user/firstname/text()")
	apellidos = doc.xpath("//user/lastname/text()")
	for i in range(len(nombres)):
		nombres[i] = nombres[i] + " " + apellidos[i]
	return nombres

print(usuariosyprofes(doc))