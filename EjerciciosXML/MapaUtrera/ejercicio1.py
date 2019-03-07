from lxml import etree
doc = etree.parse('utrera.xml')

def callesutrera(doc):
	return doc.xpath('//way/tag[@k="highway"]/../@id')

print (callesutrera(doc))