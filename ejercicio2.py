class libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    
    def mostrarInformacion(self):
        print(f'El título del libro es: {self.titulo}')
        print(f'El autor del libro es {self.autor}')
        print(f'El año de publicación fue: {self.año}')

    def es_antiguo (self):
        return self.año < 2000
    
libro1 = libro("Rayuela", "Cortazar", 1963)

libro1.mostrarInformacion()

if libro1.es_antiguo:
    print("El libro es antiguo ")
else:
    print("El libro es nuevo ")