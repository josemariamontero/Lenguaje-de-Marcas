lista = []
from urllib.request import urlopen
response = urlopen('http://tiempoytemperatura.es/espana/sevilla/dos-hermanas.html')
lineas=response.readlines()

for i in lineas:
	lista.append(str(i).strip("b"))

for i in lista:
	ahora = "<td>Ahora</td>"
	if ahora in i:
		indice = lista.index(i)

temperatura = lista[indice + 2].split("<")
humedad = lista[indice + 7].split("<")
presion = lista[indice + 8].split("<")

print ("La temperatura de Dos Hermanas es:",temperatura[1].strip('td class="temp">').strip('&deg;'),"ºC")
print ("La humedad de Dos Hermanas es:",humedad[1].strip('td>'))
print ("La presión de Dos Hermanas es:",presion[1].strip('td>'))