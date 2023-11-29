#Pedir el nombre y los dos apellidos de una persona
#y mostrar las iniciales

nombre = input("Dime tu nombre")
apellido1 = input("dime tu primer apellido")
apellido2 = input("dime tu segundo apellido")

inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]

inicial = inicial.upper()
print("Las iniciales son: " ,inicial)
