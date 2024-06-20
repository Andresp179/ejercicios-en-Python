def Suma(*numeros):
   resultado=0

   for i in numeros:
     resultado+=i
    
   return resultado


print(Suma(3,5,9))