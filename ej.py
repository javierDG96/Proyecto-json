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


def dur_canciones(prueba,cancion):
	duracion=[]
	for i in range(0,49):
		if prueba["tracks"]["items"][i]["track"]["name"]==cancion:
			duracion.append(prueba["tracks"]["items"][i]["track"]["duration_ms"])
	return duracion

def canc_artista(prueba,artista):
	canciones=[]
	for i in range(0,49):
		if prueba["tracks"]["items"][i]["track"]["artists"][0]["name"] ==artista:
			canciones.append(prueba["tracks"]["items"][i]["track"]["name"])
	return canciones

			
def popu_canc(prueba):
 	canciones=[]
 	tipo=[]
 	for i in range(0,49):
 		if prueba["tracks"]["items"][i]["track"]["popularity"] > 40:
 			canciones.append(prueba["tracks"]["items"][i]["track"]["name"])
 			tipo.append(prueba["tracks"]["items"][i]["track"]["album"]["album_type"])
 	return zip(canciones,tipo)




