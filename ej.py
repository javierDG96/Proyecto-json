import json

def listar_auto(prueba):
	autores=[]
	for i in range(0,49):
		autores.append(prueba["tracks"]["items"][i]["track"]["artists"][0]["name"])
		if len(prueba["tracks"]["items"][i]["track"]["artists"]) > 1:
			autores.append(prueba["tracks"]["items"][i]["track"]["artists"][1]["name"])
	return set(autores)
	
with open("canciones.json") as fichero:
		prueba = json.load(fichero)	
		
		print(listar_auto(prueba))
	
	
