class Animal:
    def __init__(self, nombre):
        print("se activo el construcuto")
        self.nombre=nombre

    def setnombre(self, nombre):
        self.nombre=nombre

    def getnombre (self):
        return self.nombre
    
        

ob=Animal(" gato ")
obj=Animal(" pantera ")
obj.