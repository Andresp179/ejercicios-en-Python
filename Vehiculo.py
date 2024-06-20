class Vehiculo:

    def __init__(self,color,ruedas,tipo):
        self.color=color
        self.ruedas=ruedas
        self.tipo=tipo


    def __str__(self):
        return "Color: "  + self.color + " , Ruedas " + str(self.ruedas) + " ,tipo: "+self.tipo
    

class Coche(Vehiculo):
    def __init__(self, color, ruedas, tipo,velocidad):
        super().__init__(color, ruedas, tipo)
        self.velocidad=velocidad

    def __str__(self):
        return super().__str__() +' Velocidad en kms/hora: '+str(self.velocidad)





vehiculo= Vehiculo('Red', 4,'Camioneta')
print("La descripcion es: ",vehiculo)

coche=Coche('Yellow',4,'Campero', 70)
print(coche)
