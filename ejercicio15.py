#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide 
#realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

a = int(input("introduce el valor de la variable A: "))
b = int(input("introduce el valro de la variable B: "))
aux = a
a = b
b = aux
print("Nuevo valro de A: ", a)
print("Nuevo valro de B: ", b)
