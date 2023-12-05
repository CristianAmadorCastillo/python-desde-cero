
cont = 0
posicion = 0
cad = input("Introduce una cadena: ")
#elimino los posibles espacios al principio y al final de la cad
cad = cad.strip()
#busco espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
	cont = cont + 1
	#No tengo en cuenta los pisbibles eapcios entre las palabras
	while cad[posicion + 1] == " ":
		posicion = posicion + 1
	posicion = cad.find(" ", posicion + 1)
print("La frase tiene",cont + 1,"palabras.")

