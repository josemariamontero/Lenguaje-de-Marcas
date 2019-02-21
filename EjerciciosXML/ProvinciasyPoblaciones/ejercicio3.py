def totalpob_provincias(doc):
	lista = []
	nombrepoblacion = doc.xpath("//nombre/text()")
	for provincia in doc.xpath("//provincia"):
		total_localidades = provincia.xpath('count(./localidades/localidad)')
		lista.append(int(total_localidades))
	return zip(nombrepoblacion,lista)

from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

for i,x in totalpob_provincias(doc):
	print("Provincia:",i,"=>","Poblaciones:",x)