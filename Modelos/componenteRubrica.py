from enum import Enum


class ComponenteRubrica(Enum):
    ACD = "ACD"
    APE = "APE"
    AA = "AA"
    EVALUACION = "EVALUACION"

    def __str__(self):
        return self.value