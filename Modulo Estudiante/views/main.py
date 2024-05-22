import sys
sys.path.append('../')
from controller.materiaDaoControl import MateriaDaoControl

mt = MateriaDaoControl()

try:
    mt._materia._id = 1
    mt._materia._nombre = 'Matematicas'
    mt._materia._numeroHoras = 5
    mt.save

except Exception as error:
    print(error)