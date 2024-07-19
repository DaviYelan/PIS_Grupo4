import sys
sys.path.append('../')

from controllers.estudianteDaoControl import EstudianteDaoControl
from controllers.facultadDaoControl import FacultadDaoControl
from controllers.universidadDaoControl import UniversidadDaoControl
from controllers.materiaDaoControl import MateriaDaoControl
from controllers.mallaDaoControl import MallaDaoControl
from controllers.unidadDaoControl import UnidadDaoControl
from controllers.cursaDaoControl import CursaDaoControl
from controllers.periodoAcademicoDaoControl import PeriodoAcademicoDaoControl
from controllers.personaDaoControl import PersonaDaoControl

fdc = FacultadDaoControl()
udc = UniversidadDaoControl()
mdc = MateriaDaoControl()
mcd = MallaDaoControl()
ucd = UnidadDaoControl()
cdc = CursaDaoControl()
padc = PeriodoAcademicoDaoControl()  
edc = EstudianteDaoControl()
pdc = PersonaDaoControl() 

try:
    # Comenta estas líneas si no quieres ejecutarlas en este momento
    # fdc._facultad._nombre = "Ingenieria"
    # fdc.save

    # udc._universidad._nombre = "Universidad Nacional de Ingenieria"
    # udc._universidad._direccion = "Av. Túpac Amaru 210"
    # udc._universidad._ciudad = "Loja"
    # udc.save

    # mdc._materia._nombre = "Matematicas"
    # mdc._materia._ciclo = "Primer ciclo"
    # mdc._materia._numeroHoraSemana = 4
    # mdc.save

    # mcd._malla._nombre = "Malla de Computación"
    # mcd._malla._estado = "Activa"
    # mcd.save

    # ucd._unidad._nombre = "Primer Unidad"
    # ucd._unidad._duracionSemanas = 260
    # ucd.save

    # padc._periodoAcademico._nombre = "Primer Periodo"
    # padc._periodoAcademico._fechaInicio = "2021-01-01"
    # padc._periodoAcademico._fechaFin = "2021-07-01"
    # padc._periodoAcademico._tipoEstado = "Activo"
    # padc.save

    # cdc._cursa._idEstudiante._nombre = "Juan"
    # cdc._cursa._idEstudiante._apellido = "Perez"
    # cdc._cursa._idEstudiante._cedula = "1104567890"
    # cdc._cursa._idEstudiante._direccion = "Av. Túpac Amaru 210"
    # cdc._cursa._idEstudiante._telefono = "0987654321"
    # cdc._cursa._idEstudiante._estado = "Primer Matricula"
    # cdc._cursa._paralelo = "A"
    # cdc.save

    # pdc._persona._nombre = "Juan"
    # pdc._persona._apellido = "Perez"
    # pdc._persona._cedula = "1104567890"
    # pdc._persona._direccion = "Av. Túpac Amaru 210"
    # pdc._persona._telefono = "0987654321"
    # pdc.save
    edc._estudiante._estado = "PRIMERA MATRICULA"
    edc._estudiante._tipo = "Regular"
    edc.save

except Exception as error:
    print("Errores")
    print(error)


