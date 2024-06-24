import sys
sys.path.append('../')

from control.tda.linked.linkedList import Linked_List
from control.estudianteDaoControl import estudianteDaoControl
from control.docenteDaoControl import docenteDaoControl
from control.materiaDaoControl import materiaDaoControl

import random
import time

listaNumber = Linked_List()
listaString = Linked_List()
try:
    fact = estudianteDaoControl()
    doc= docenteDaoControl()
    mdc= materiaDaoControl()


    fact._estudiante._nombre = "Juan"
    fact._estudiante._apellido = "Valadat"
    fact._estudiante._direccion = "Mexico y Venezuela"
    fact._estudiante._fechaNacimiento = "2021-10-10"
    fact._estudiante._genero = "Masculino"
    fact._estudiante._telefono = "1234567890"
    fact._estudiante._tipoIdentificacion = "Pasaporte"
    fact._estudiante._cedula = "1900805852"
    fact.save

    fact._estudiante._nombre = "Juan"
    fact._estudiante._apellido = "Valadat"
    fact._estudiante._direccion = "Mexico y Venezuela"
    fact._estudiante._fechaNacimiento = "2021-10-10"
    fact._estudiante._genero = "Masculino"
    fact._estudiante._telefono = "1234567890"
    fact._estudiante._tipoIdentificacion = "Pasaporte"
    fact._estudiante._cedula = "1900805852"
    fact.save

    fact._estudiante._nombre = "Juan"
    fact._estudiante._apellido = "Valadat"
    fact._estudiante._direccion = "Mexico y Venezuela"
    fact._estudiante._fechaNacimiento = "2021-10-10"
    fact._estudiante._genero = "Masculino"
    fact._estudiante._telefono = "1234567890"
    fact._estudiante._tipoIdentificacion = "Pasaporte"
    fact._estudiante._cedula = "1900805852"
    fact.save


    doc._docente._nombre = "Juan"
    doc._docente._apellido = "Valadat"
    doc._docente._direccion = "Mexico y Venezuela"
    doc._docente._fechaNacimiento = "2021-10-10"
    doc._docente._genero = "Masculino"
    doc._docente._telefono = "1234567890"
    doc._docente._tipoIdentificacion = "Pasaporte"
    doc._docente._cedula = "1900805852"
    doc.save
    
    
    mdc._materia._nombre = "Matematica"
    mdc._materia._codigo = "06060"
    mdc._materia._horaSemanal = 12
    mdc._materia._nombCiclo = "Ciclo 2"
    mdc.save

except Exception as e:
    print(f"Error: {e}")