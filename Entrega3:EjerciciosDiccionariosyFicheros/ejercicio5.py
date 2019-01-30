with open("zipsjson.txt","r") as fichero:
    diccionario = fichero.readlines()
    #print (diccionario)
Numero_de_codigo_postales = 1
estado = diccionario["state"]
for linea in codigo:
    diccionario = json.loads(linea)
    if diccionario["state"] == estado:
            Numero_de_codigo_postales = Numero_de_codigo_postales + 1
    else:
            print ("Estado:",estado, "Números De Código postal",Numero_de_codigo_postales)
            estado = diccionario["state"]
            Numero_de_codigo_postales = 0

print ("Estado:",estado, "Codigo postal",Numero_de_codigo_postales)

codigo=open("zips.json","r")
ciudad=""
estado=""

while ciudad != "AKASKA":
    linea = codigo.readline()
    diccionario = json.loads(linea)
    ciudad = diccionario["city"]
    estado = diccionario["state"]

print (diccionario)
geolocalizacion = diccionario["loc"]
latitud = geolocalizacion[0]
longitud = geolocalizacion[1]
print ("http://www.openstreetmap.org/search?query=akaska#map=15/45.3325/-100.1207/%s/%s" % (latitud,longitud))
print ("Las coordenadas de AKASKA ", "Latitud:45.3325", "Longitud:-100.1207")
