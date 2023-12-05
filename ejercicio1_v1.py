#Crea uan aplicaciones que pida un numero y calcule su factorial
# un numero es el producto de todos los enteros entr 1 y el propio numero.

resultado = 1;
num=int(input("Dime un numero: "))
contador = 2;
while contador <= num:
	resultado = resultado * contador;
	contador = contador + 1;
print("El resultado es ", resultado)
