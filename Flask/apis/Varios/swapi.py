import requests
url_base = "https://swapi.co/api/"

r = requests.get(url_base+"people/")

if r.status_code == 200:
	doc = r.json()
	for i in doc["results"]:
		print (i["name"])

else:
	print ("error en la peticion")