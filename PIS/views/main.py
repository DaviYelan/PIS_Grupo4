import sys
sys.path.append('../')
from controllers import personaDaoControl
from controllers.facultadDaoControl import FacultadDaoControl
from controllers.universidadDaoControl import UniversidadDaoControl
from controllers.materiaDaoControl import MateriaDaoControl
from controllers.mallaDaoControl import MallaDaoControl
from controllers.unidadDaoControl import UnidadDaoControl
from controllers.cursaDaoControl import CursaDaoControl
from controllers.periodoAcademicoDaoControl import PeriodoAcademicoDaoControl
from controllers.personaDaoControl import PersonaDaoControl
from controllers.estudianteDaoControl import EstudianteDaoControl
from controllers.docenteDaoControl import DocenteDaoControl

fdc = FacultadDaoControl()
udc = UniversidadDaoControl()
mdc = MateriaDaoControl()
mcd = MallaDaoControl()
ucd = UnidadDaoControl()
cdc = CursaDaoControl()
padc = PeriodoAcademicoDaoControl()
pdc = PersonaDaoControl()
edc = EstudianteDaoControl()
dc = DocenteDaoControl()
try:
#    fdc._facultad._nombre = "Ingenieria"
#    fdc.save

#    udc._universidad._nombre = "Universidad Nacional de Ingenieria"
#    udc._universidad._direccion = "Av. Túpac Amaru 210"
#    udc._universidad._ciudad = "Loja"
#    udc.save

#    mdc._materia._nombre = "Matematicas"
#    mdc._materia._ciclo = "Primer ciclo"
#    mdc._materia._numeroHoraSemana = 4
#    mdc.save

#    mcd._malla._nombre = "Malla de Computación"
#    mcd._malla._estado = "Activa"
#    mcd.save

#    ucd._unidad._nombre = "Primer Unidad"
#    ucd._unidad._duracionSemanas = 260
#    ucd.save
    #  pdc._periodoAcademico._nombre = "Primer Periodo"
    #  pdc._periodoAcademico._fechaInicio = "2021-01-01"
    #  pdc._periodoAcademico._fechaFin = "2021-07-01"
    #  pdc._periodoAcademico._tipoEstado = "Activo"
    #  pdc.save

    #  cdc._cursa._idEstudiante._nombre = "Juan"
    #  cdc._cursa._idEstudiante._apellido = "Perez"
    #  cdc._cursa._idEstudiante._cedula = "1104567890"
    #  cdc._cursa._idEstudiante._direccion = "Av. Túpac Amaru 210"
    #  cdc._cursa._idEstudiante._telefono = "0987654321"
    #  cdc._cursa._idEstudiante._estado = "Primer Matricula"
    #  cdc._cursa._paralelo = "A"
    #  cdc.save
    #  pdc._persona._nombre = "Juan"
    #  pdc._persona._apellido = "Perez"
    #  pdc._persona._telefono = "0987654321"
    #  pdc._persona._correo = "juan.perez@unl.edu.ec"
    #  pdc._persona._fecha = "2021-01-01"
    #  pdc._persona._genero = "Masculino"
    #  pdc._persona._tipoIdentificacion = "Cedula"
    #  pdc.save
    #  dc._docente._nombre = "Juan"
    #  dc._docente._apellido = "Perez"
    #  dc._docente._fecha = "2021-01-01"
    #  dc._docente._telefono = "0987654321"
    #  dc._docente._correo = "juan.perez@unl.edu.ec"
    #  dc._docente._genero = "Masculino"
    #  dc._docente._tipoIdentificacion = "Cedula"
    #  dc._docente._tituloCuartoNivel = "Ingeniero en Sistemas"
    #  dc._docente._especialidad = "Ingeniero en Sistemas"
    #  dc._docente._cubiculo = "A-1"
    #  dc.save
    edc._estudiante._nombre = "Darwin"
    edc._estudiante._apellido = "Perez"
    edc._estudiante._fecha = "2021-01-02"
    edc._estudiante._genero = "Masculino"
    edc._estudiante._telefono = "0987654321"
    edc._estudiante._correo = "darwin.perez@unl.edu.ec"
    edc._estudiante._orden = "SEGUNDA MATRICULA"
    edc._estudiante._ciclo = 2
    edc.save
    
except Exception as error:
    print("Errores")
    print(error)

