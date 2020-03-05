import json

def listar_auto(prueba):
	autores=[]
	for i in range(0,49):
		autores.append(prueba["tracks"]["items"][i]["track"]["artists"][0]["name"])
		if len(prueba["tracks"]["items"][i]["track"]["artists"]) > 1:
			autores.append(prueba["tracks"]["items"][i]["track"]["artists"][1]["name"])
	return set(autores)
	
	
def contar_canciones(prueba):
	canciones=[]
	for i in range(0,50):
		canciones.append(prueba["tracks"]["items"][i]["track"]["name"])

	return len(canciones)

	

