import requests,json
url_base = "http://api.elpais.com/ws/LoteriaNavidadPremiados"
numero = int(input("Introduce un numero de loteria: "))
payload={"n":numero}

r = requests.get(url_base,params=payload)
if r.status_code == 200:
	doc=r.text.split("=")[1]
	doc2 = json.loads(doc)
	print (doc2["premio"])

