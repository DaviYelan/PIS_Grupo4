import enum
class EnumEstadoEstudiante(enum.Enum):
    PRIMERA = "PRIMERA MATRICULA"
    SEGUNDA = "SEGUNDA MATRICULA"
    TERCERA = "TERCERA MATRICULA"

    def getValue(self):
        return self.value
    
    @classmethod
    def from_str(cls, value):
        for enum_type in cls:
            if enum_type.value == value:
                return enum_type
        raise ValueError(f"Invalid value for EnumEstadoEstudiante: {value}")
    
  