def identificadores(lista,doc):
	lista = []
	for i in lista:
		provincias = doc.xpath('//provincia[@id="%s"]/nombre/text()' % i)
		localidades = doc.xpath('//provincia[@id="%s"]/localidades/localidad/text()' % i)
		lista.append([nombre[0],localidades])
	return lista

from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

lista = []

identificador = int(input("Dime el identificador de la provincia: "))

while identificador != 0:
	lista.append(identificador)
	identificador = int(input("Dime el identificador de la provincia: "))

lista = identificadores(lista,doc)

for i in lista:
	provincia = i[0]
	localiad = i[1]
	print (provincia)
	for x in localiad:
		print (x)