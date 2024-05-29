import sys
sys.path.append('../')
from controller.materiaDaoControl import MateriaDaoControl

mt = MateriaDaoControl()

try:
    mt._materia._nombre = 'Base de Datos'
    mt._materia._numeroHoraSemana = 3
    mt.save

except Exception as error:
    print(error)