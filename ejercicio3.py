class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)
    
    def es_aprobado(self):
        prom = self.promedio()
        return prom >= 60

estudiante1 = Estudiante ("Mario", 18, [6, 7, 8, 4])

estudiante1.promedio()

if estudiante1.es_aprobado:
    print(f'El estudiante {estudiante1.nombre} ha aprobado')
else:
    print(f'El estudiante {estudiante1.nombre} ha desaprobado')