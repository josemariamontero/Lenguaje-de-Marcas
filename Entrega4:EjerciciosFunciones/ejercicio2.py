def pasar_a_segundos(hora,minutos,segundos):
	return hora * 3600 + minutos * 60 + segundos

def calcular_coste(segundos,tarifa):
	coste = segundos * tarifa
	return coste

def convertir_a_euros(coste):
	euros = round(coste / 100)
	centimos = coste % euros
	return euros,centimos 

lista_llamadas = []
contador = 0
tarifa = 3

with open("comunicaciones.txt","r") as fichero:
	comunicaciones = fichero.readlines()


for i in comunicaciones:
	i = i.replace("\n","")
	hora = int(i.split(":")[0])
	minutos = int(i.split(":")[1])
	segundos = int(i.split(":")[2])
	segundos2 = pasar_a_segundos(hora,minutos,segundos)
	costes = calcular_coste(segundos2,tarifa)
	euros,centimos = convertir_a_euros(costes)
	lista_llamadas.append(costes)
	contador = contador + 1
	print ("Llamada:",contador,"Euros:",euros,"Centimos:",centimos)	

sumatotal = sum(lista_llamadas)
euros,centimos = convertir_a_euros(sumatotal)
print ("Coste total de las comunicaciones es de:",euros,"euros y",centimos,"centimos")