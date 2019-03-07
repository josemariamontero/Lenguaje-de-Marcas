from lxml import etree
doc = etree.parse('utrera.xml')

def nodos_utrera(doc):
	nodos = doc.xpath('//node[@uid="384182" and count(tag)>0]/@id')
	return nodos

print (nodos_utrera(doc))