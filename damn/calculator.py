import itertools
from .value import Value, DecimalValue
from .lib import wolfram_calculate


def convert_kv(s: str) -> tuple[str, float]:
    s = s.strip().split(" equals ")
    n, v = s
    v = float(v.replace("minus ", "-").replace("negative ", "-"))
    return n, round(v, 2)


class Calculator:
    def __init__(self, apps: list[str]):
        self.apps = itertools.cycle(apps)

    async def calculate(self, data: dict[str, Value], formula: str) -> DecimalValue:
        s = ", ".join(
            (f"{k} = {v.get_formula_representation()}" for k, v in data.items())
        )
        result = await wolfram_calculate(next(self.apps), s + ", " + formula)
        variables = dict(
            (
                convert_kv(v)
                for v in result.replace(
                    " and ",
                    "",
                ).split(",")
            )
        )
        for variable in data:
            variables.pop(variable)
        return DecimalValue(list(variables.values())[0])
