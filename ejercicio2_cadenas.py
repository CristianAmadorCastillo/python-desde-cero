#Programa qeu compreuba si una cadena es leida por teclado
# comienza por una subcadena introducida por teclado.

cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")
if cad.startswith(subcad):
	print("La cadena comienza por la subcadena")
else:
	print("La cadena no comienza por la subcadena")
