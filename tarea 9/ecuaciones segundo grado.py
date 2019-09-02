import math
print('teniendo en cuenta la ecuacion ax^2+bx+c')
a=int(input("introduce el valor a: "))
b=int(input("introduce el valor b: "))
c=int(input("introduce el valor c: "))

d=(b*b)-4*a*c
if d<0:
    print("no existen soluciones reales")
else:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)

    print("----soluciones----")
    print("solucion de x1: ",x1)
    print("solucion de x2: ",x2)