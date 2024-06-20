p1=float(input("Ingrese nota practica 1: "))
p2=float(input("Ingrese nota practica 2: "))
p3=float(input("Ingrese nota practica 3: "))

print('Nota primer practica es: ',p1,' Nota segunda practica es:',p2,' Nota tercera practica es: ',p3)

pp=float((p1+p2+p3)/3)
print('Su promedio general en practicas es: ',pp)

ep=float(input('Ingrese nota del examen parcial: '))
ef=float(input('Ingrese nota examen final: '))
notaFinal=((pp+(2*ep)+(3*ef))/6)
print('Su nota final es: ',notaFinal)