import enum
class EnumTipoIdentificacion(enum.Enum):
    CEDULA = "CEDULA"
    PASAPORTE = "PASAPORTE"
    RUC = "RUC"
    LICENCIA = "LICENCIA CONDUCIR"

    def getValue(self):
        return self.value