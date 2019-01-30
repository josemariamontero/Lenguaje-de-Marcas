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

num_comunicaciones = int(input("Cuantas comunicaciones has realizado?: "))
tarifa = int(input("Dime la tarifa: "))

for i in range(1,num_comunicaciones + 1):
	hora = int(input("Dime la hora: "))
	minutos = int(input("Dime los minutos: "))
	segundos = int(input("Dime los segundos: "))
	segundos2 = pasar_a_segundos(hora,minutos,segundos)
	costes = calcular_coste(segundos2,tarifa)
	euros,centimos = convertir_a_euros(costes)
	lista_llamadas.append(costes)
	print ("Llamada:",i,"Euros:",euros,"Centimos:",centimos)

sumatotal = sum(lista_llamadas)
euros,centimos = convertir_a_euros(sumatotal)
print ("Coste total de las comunicaciones es de:",euros,"euros y",centimos,"centimos")