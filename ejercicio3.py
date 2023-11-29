#Calcular la hipotenusa de un triangulo rectangulo
#dados su catetos.

import math
cateto1 = float(input("Introduce el cateto1: "))
cateto2 = float(input("Introduce el cateto2: "))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print("La hipotenusa es: %.2f " % hipotenusa)
