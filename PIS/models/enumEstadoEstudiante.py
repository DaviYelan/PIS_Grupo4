import enum
class EnumEstadoEstudiante(enum.Enum):
    PRIMERAMATRICULA = "PRIMERA MATRICULA"
    SEGUNDAMATRICULA = "SEGUNDA MATRICULA"
    TERCERAMATRICULA = "TERCERA MATRICULA"

    def getValue(self):
        return self.value