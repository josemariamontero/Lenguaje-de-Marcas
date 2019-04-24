import requests
url_base = "http://dit.gonzalonazareno.org/redmine/"

r = requests.get(url_base+"projects.json/")

if r.status_code == 200:
	doc = r.json()
	for i in doc["projects"]:
		print (i["name"])

else:
	print ("error en la peticion")