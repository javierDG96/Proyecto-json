import json
with open("canciones.json") as fichero:
		prueba = json.load(fichero)	

from ej import contar_canciones,dur_cancion,canc_autor,listar_auto,popu_canc

while True:
    print("Menú de ejercicios")
    print("   1.Listar todos los autores que hay")
    print("   2.Contar las canciones que tiene el documento")
    print("   3.Lista la duracion de la cancion pedida")
    print("   4.Buscar un artista y que te diga todas sus canciones")
    print("   5.Lista las canciones que tengan una popularidad mayor que 40 y el tipo al que pertenecen")
    print("   0.Salir")
    # ingresar una opcion
    opcion = int(input("Elija una opción (0-5): "))
    if opcion==1:
    	for autores in(listar_auto(prueba)):
    		print(autores)