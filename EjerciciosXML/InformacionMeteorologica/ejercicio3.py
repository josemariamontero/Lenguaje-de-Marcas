from lxml import etree
doc = etree.parse('sevilla.xml')

def pronostico7dias(doc):
	pro={}
	pronostico=doc.xpath("//pronostico_dias/dia/@fecha")
	for dia in pronostico:
		pro[dia]=(doc.xpath('//pronostico_dias/dia[@fecha="%s"]/maxima/text()'%dia)[0],doc.xpath('//pronostico_dias/dia[@fecha="%s"]/minima/text()'%dia)[0])

	return pro

pronostico3 = pronostico7dias(doc)

for i,x in pronostico3.items():
	print(i,"=>","Maxima:",x[0],"Minima:",x[1])
	