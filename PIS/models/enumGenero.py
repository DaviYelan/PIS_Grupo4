import enum
class EnumGenero(enum.Enum):
    MASCULINO = "MASCULINO"
    FEMENINO = "FEMENINO"
    OTRO = "OTRO"

    def getValue(self):
        return self.value