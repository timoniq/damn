from abc import ABC, abstractmethod
from damn.value.abc import Value
from damn.error import ParseError
import typing


NewValues = typing.Dict[str, Value]


class Definition(ABC):
    @classmethod
    @abstractmethod
    def parse(cls, s: str) -> typing.Optional["Definition"]:
        pass

    @abstractmethod
    def generate(self) -> NewValues:
        pass

    @classmethod
    def get_error(cls, err: str = ""):
        return ParseError(cls, err)
