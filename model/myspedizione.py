import datetime
from dataclasses import dataclass


@dataclass
class MySpedizione:
    id_hub_origine: int
    id_hub_destinazione: int
    conteggio: int
    somma: float

    def __eq__(self, other):
        return isinstance(other, MySpedizione) and self.id_hub_origine == other.id_hub_destinazione and self.id_hub_destinazione == other.id_hub_destinazione

    def __str__(self):
        return f"H_O = {self.id_hub_origine}, H_D = {self.id_hub_destinazione}, count = {self.conteggio}, sum = {self.somma}"

    def __repr__(self):
        return f"H_O = {self.id_hub_origine}, H_D = {self.id_hub_destinazione}, count = {self.conteggio}, sum = {self.somma}"


