import enum
class EnumComponenteRubrica(enum.Enum):
    ACD = "ACD"
    APE = "APE"
    AA = "AA"
    EVALUACION = "EVALUACION"

    def getValue(self):
        return self.value