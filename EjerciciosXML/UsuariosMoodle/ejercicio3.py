from lxml import etree
doc = etree.parse('users.xml')

def correos(doc):
	correos = doc.xpath("//user[contains(lastip,172.22)=False]/email/text()")
	return correos

print (correos(doc))