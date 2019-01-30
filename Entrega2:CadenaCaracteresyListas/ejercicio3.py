temperaturas = '''Utrera,29,12
Dos Hermanas,32,14
Sevilla,30,15
Alcala de Guadaira,31,14'''

utrera = []
dos_hermanas = []
sevilla = []
alcala = []

utrera = temperaturas.strip("\n")[0:12].split(",")
maximautrera = utrera[1]
minimautrera = utrera[2]
mediautrera = (int(maximautrera) + int(minimautrera)) / 2

dos_hermanas = temperaturas.strip("\n")[13:31].split(",")
maximados_hermanas = dos_hermanas[1]
minimados_hermanas = dos_hermanas[2]
mediados_hermanas = (int(maximados_hermanas) + int(minimados_hermanas)) / 2

sevilla = temperaturas.strip("\n")[32:45].split(",")
maximasevilla = sevilla[1]
minimasevilla = sevilla[2]
mediasevilla = (int(maximasevilla) + int(minimasevilla)) / 2

alcala = temperaturas.strip("\n")[46:].split(",")
maximaalcala = alcala[1]
minimaalcala = alcala[2]
mediaalcala = (int(maximaalcala) + int(minimaalcala)) / 2

nombre = input("Introduce el nombre del pueblo del que desea conocer la temperatura media: ")

if nombre == utrera[0]:
	print ("La maxima es",maximautrera,"y la minima es", minimautrera)
elif nombre == dos_hermanas[0]:
	print ("La maxima es",maximados_hermanas,"y la minima es", minimados_hermanas)
elif nombre == sevilla[0]:
	print ("La maxima es",maximasevilla,"y la minima es", minimasevilla)
elif nombre == alcala[0]:
	print ("La maxima es",maximaalcala,"y la minima es", minimaalcala)
else:
	print ("No existe las temperaturas de esa población")