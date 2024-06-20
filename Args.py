def multiplica(*numeros):
    resultado=1

    for number in numeros:
        
        resultado*=number       
    return resultado    


print(multiplica(2,6,4,9))       