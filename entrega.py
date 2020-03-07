import json
with open("canciones.json") as fichero:
		prueba = json.load(fichero)	

from ej import contar_canciones,listar_auto,dur_canciones

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
    elif opcion==2:
    	print("Hay",contar_canciones(prueba),"canciones en el documento")
    
    elif opcion==3:
    	cancion=input("Dime el nombre de la cancion:")
    	for duracion in dur_canciones(prueba,cancion):
    		print("La duracion es",round(duracion/60000 ,2),"min")