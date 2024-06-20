class Cubo:

    def __init__(self,alto, ancho, profundo):
        self.alto=alto
        self.ancho=ancho
        self.profundo=profundo

    def cubo(self):
        return alto*ancho*profundo

alto=int(input("Introduzca altura: "))
ancho=int(input("Introduzca anchura: "))
profundo=int(input("Introduzca profundidad: "))    

Cubo1=Cubo(alto,ancho,profundo)
print(f'Volumen: {Cubo1.cubo()}') 