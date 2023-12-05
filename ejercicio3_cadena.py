#Pide una cadena y un caracter por teclado
#Valida que sea un caracter y muestra cuentas veces aparece el caracter

cad = input("Introduce la cadena: ")
while True:
	car = input("Introduce un caracter ")
	if len(car)>1:
		print("Me tienes qeu dar un solo caracter")
	if len(car) == 1: break

print("En la cadena ",cad,"aparecen",cad.count(car),"veces el caracter")
