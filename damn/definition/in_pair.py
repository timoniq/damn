from .abc import Definition, NewValues
from damn.value import Value, DecimalValue
import typing
import re
import random


class InPairDefinition(Definition):
    pattern = re.compile(r"\((.+)\) in \[(.+)]")
    pair_pattern = re.compile(r"\(([^()]+)\)")

    def __init__(
        self, names: typing.List[str], pairs: typing.List[typing.Tuple[Value, ...]]
    ):
        self.names = names
        self.pairs = pairs

    @classmethod
    def parse(cls, s: str) -> typing.Optional["InPairDefinition"]:
        m = re.match(cls.pattern, s)
        if not m:
            return None
        m = m.groups()
        names = list(map(lambda x: x.strip(" "), m[0].split(",")))
        pairs = []
        for pair in re.finditer(cls.pair_pattern, m[1]):
            pair = pair.group(1)
            mapping = map(lambda x: x.strip(" "), pair.split(","))
            values = map(lambda x: DecimalValue.from_str(x), mapping)
            pairs.append(tuple(values))
        return cls(names, pairs)

    def generate(self) -> NewValues:
        pair = random.choice(self.pairs)
        return dict(zip(self.names, pair))
