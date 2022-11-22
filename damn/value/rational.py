from .abc import Value
from damn.utils import braced


class RationalValue(Value):
    def __init__(self, nom: Value, denom: Value):
        self.nom = nom
        self.denom = denom

    def get_common_representation(self) -> str:
        return (
            self.nom.get_common_representation()
            + "/"
            + self.denom.get_common_representation()
        )

    def get_formula_representation(self) -> str:
        return braced(
            self.nom.get_formula_representation()
            + "/"
            + self.denom.get_formula_representation()
        )

    def cmp_to_user_input(self, s: str) -> bool:
        s = s.replace(" ", "").replace(",", ".")
        return (
            s == self.get_common_representation()
            or s == self.get_formula_representation()
        )
