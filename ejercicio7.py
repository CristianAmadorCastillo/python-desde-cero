#Realizar una lgoritmo que muestre la tabla de multiplicar de un numero introducido

tabla = int(input("De que numero quieres mostrar la tabla mult"))
for num in range(1, 11):
	print("%d * %d = %d" % (num,tabla,num*tabla))
