from lxml import etree
doc = etree.parse('utrera.xml')

def nombre_calles(doc):
	nombres = doc.xpath('//way/tag[@k="highway"]/../tag[@k="name"]/@v')
	return nombres

print (nombre_calles(doc))