import enum
class EnumEstadoPeriodo(enum.Enum):
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"
    FINALIZADO = "FINALIZADO"

    def getValue(self):
        return self.value