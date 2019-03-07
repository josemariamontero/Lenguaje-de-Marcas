from lxml import etree
doc = etree.parse('utrera.xml')

def supermercados(doc):
	supermercados = doc.xpath('count(//way/tag[@k="shop"]/../tag[@v="supermarket"])')
	return supermercados

print (supermercados(doc))