from .abc import Definition, NewValues
from damn.value import Value, DecimalValue
import re
import typing
import random


class InSingleDefinition(Definition):
    pattern = re.compile(r"(\w+) in \[(.+)]")

    def __init__(self, name: str, values: typing.List[Value]):
        self.name = name
        self.values = values

    @classmethod
    def parse(cls, s: str) -> typing.Optional["InSingleDefinition"]:
        m = re.match(cls.pattern, s)
        if not m:
            return None
        m = m.groups()
        values = []
        for value in m[1].split(","):
            values.append(DecimalValue.from_str(value.rstrip(" ")))
        return cls(m[0], values)

    def generate(self) -> NewValues:
        return {self.name: random.choice(self.values)}
