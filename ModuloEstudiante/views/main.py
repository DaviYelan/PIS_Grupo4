import sys
sys.path.append('../')
from controller.materiaDaoControl import MateriaDaoControl

mt = MateriaDaoControl()

try:
    mt._materia._nombre = 'Base de Datos'
    mt._materia.__numeroHoraSemana = 5
    mt.save

except Exception as error:
    print(error)