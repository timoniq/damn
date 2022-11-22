from .abc import Value
import typing


class DecimalValue(Value):
    def __init__(self, v: typing.Union[int, float]):
        self.v = v

    def get_common_representation(self) -> str:
        return str(self.v)

    def get_formula_representation(self) -> str:
        return str(self.v)

    @classmethod
    def from_str(cls, s: str) -> "DecimalValue":
        return cls(int(s) if s.isdigit() else float(s))

    def cmp_to_user_input(self, s: str) -> bool:
        s = s.replace(",", ".")
        return (
            s == self.get_common_representation()
            or s == self.get_formula_representation()
        )
