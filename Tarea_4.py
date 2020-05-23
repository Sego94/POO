#TRABAJO DE CLASE 4: POO
# Una escuela tiene alumnos, cuyas características son:
# *Nombre
# *Apellido
# *Nota Matematicas
# *Nota Lengua
# *Nota Geografía
# *Promedio

# -Los alumnos pueden dar exámenes.

# La escuela también tiene profesores que tienen las siguientes características:
# *Nombre
# *Apellido
# *Materia que enseña

# -Los profesores toman exámenes y le dan al alumno una nota.

# Se deben cargar distintos alumnos y profesores, que los alumnos den exámenes que toman los profesores
# y que el resultado sea una nota. El alumno siempre debe tener un promedio (al principio las tres notas son 0).


class Alumnos():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.profesores = {'Pedro Senovilla': 'Matemáticas', 'Amalia Gómez': 'Lenguaje', 'Pedro Sánchez': 'Geografía'}
        self.notas ={'Matemáticas': 0, 'Lenguaje': 0, 'Geografía': 0}
        self.__entregar_examenes = False
    
    
    def entrega_examenes(self, entrega):
        self.__entregar_examenes = entrega
        if self.__entregar_examenes == True:
            return ('El alumno {} {}, ha entregado los exámenes'.format(self.nombre, self.apellido))
        else:
            return ('El alumno {} {}, no ha entregado los exámenes'.format(self.nombre, self.apellido))

    
    def nota_examenes(self, matematicas, lengua, geografia):
        self.notas.update({'Matemáticas': matematicas, 'Lenguaje': lengua, 'Geografía': geografia})
        print('\nEvaluaciones:')
        for profesor, materia in self.profesores.items():
            if self.__entregar_examenes == True:
                print('\nEl profesor {}, imparte la materia de {}.\nHa evaluado el exámen del alumno {} {}, su nota ha sido {}'.format(profesor, materia, self.nombre, self.apellido, self.notas.get(materia)))
            
            else:
                print('No existe evaluación de {}'.format(materia))
        
    
    def promedio(self):
        if self.__entregar_examenes == True:
            return ('\nEl promedio obtenido ha sido {0:.2f}'.format(sum(self.notas.values())/len(self.notas)))

        else:
            return ('No se han entregado los exámenes')            





alumno_1 = Alumnos('Juan', 'García')
print(alumno_1.entrega_examenes(True))
alumno_1.nota_examenes(5, 7, 3)
print(alumno_1.promedio())
print('\n********** SIGUIENTE ALUMNO **********\n')
alumno_2 = Alumnos('Rosa', 'León')
print(alumno_2.entrega_examenes(False))
alumno_2.nota_examenes(8,3,9)
print(alumno_2.promedio())