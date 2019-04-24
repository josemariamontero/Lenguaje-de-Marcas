import requests,os
url_base = "http://dit.gonzalonazareno.org/redmine/"
key = os.environ["key"]
payload={"key":key}
r = requests.get(url_base+"projects.json/",params=payload)

if r.status_code == 200:
	doc = r.json()
	for i in doc["projects"]:
		print (i["id"],"-",i["name"])

else:
	print ("error en la peticion")