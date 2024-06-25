import sys
sys.path.append('../')
from controller.materiaDaoControl import MateriaDaoControl

mt = MateriaDaoControl()

try:
    mt._materia._nombre = 'Base de Datos'
    mt._materia._numeroHoraSemana = 3
    mt.save

    mt._materia._nombre = 'Programacion'
    mt._materia._numeroHoraSemana = 4
    mt.save

except Exception as error:
    print(error)