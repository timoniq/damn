from .abc import Definition, NewValues
from damn.value import DecimalValue
import re
import typing
import random


class DomainDefinition(Definition):
    pattern = re.compile(r"(.+) > (\w+) > (.+)")

    def __init__(
        self,
        name: str,
        start: DecimalValue,
        end: DecimalValue,
        is_integer: bool = False,
    ):
        self.name = name
        self.start = start
        self.end = end
        self.is_integer = is_integer

    @classmethod
    def parse(cls, s: str) -> typing.Optional["DomainDefinition"]:
        m = re.match(cls.pattern, s)
        if not m:
            return None
        m = m.groups()
        start, name, end = list(m)
        start = DecimalValue.from_str(start)
        end = DecimalValue.from_str(end)
        return cls(name, start, end, is_integer=False)

    def generate(self) -> NewValues:
        if self.is_integer:
            result = random.randint(self.start.v, self.end.v)
        else:
            result = random.uniform(self.start.v, self.end.v)
        result = round(result, 2)
        return {self.name: DecimalValue(result)}
