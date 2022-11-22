import typing
from .definition import (
    Definition,
    InPairDefinition,
    InSingleDefinition,
    DomainDefinition,
)
from .value import Value, DecimalValue
from .lib import wolfram_calculate
import itertools

definition_types = [InPairDefinition, InSingleDefinition, DomainDefinition]


class DefinitionSet:
    def __init__(self, def_set: typing.Set[Definition]):
        self.def_set = def_set

    @classmethod
    def from_expressions(cls, expressions: typing.List[str]) -> "DefinitionSet":
        def_set = set()
        for expr in expressions:
            definition: typing.Optional["Definition"] = None
            for deft in definition_types:
                if d := deft.parse(expr):
                    definition = d
            if not definition:
                raise SyntaxError("Unable to parse expression `{}`".format(expr))
            def_set.add(definition)
        return cls(def_set)

    def get_data(self) -> typing.Dict[str, Value]:
        data = {}
        for definition in self.def_set:
            data.update(definition.generate())
        return data
