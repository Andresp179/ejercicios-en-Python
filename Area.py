class Area:

    def __init__(self,base,altura):
        self.base=base
        self.altura=altura   

    
    def sumar(self):
        return base*altura


base=int(input("Introduzca la base: "))
altura=int(input("Introduzca la altura: "))
Area1=Area(base,altura)
print(f'Suma: {Area1.sumar()}') 