import requests,os
url_base = "http://dit.gonzalonazareno.org/redmine/"
key = os.environ["key"]
payload={"key":key}

id_proyecto = ""
r = requests.get(url_base+"projects.json/",params=payload)

proyecto = input("Dime el nombre de un projecto: ")

if r.status_code == 200:
	doc = r.json()
	for i in doc["projects"]:
		nombre_proyecto = i["name"]
		if proyecto == nombre_proyecto:
			id_proyecto = i["id"]
	

payload2 = {"key":key,"project_id":id_proyecto,"limit":"5"}
r2 = requests.get(url_base+"issues.json/",params=payload2)
if r2.status_code == 200:
	doc2 = r2.json()
	for i in doc2["issues"]:
		print (i["subject"])
		print (i["assigned_to"]["name"])
else:
	print ("error en la peticion")