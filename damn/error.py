import typing

if typing.TYPE_CHECKING:
    from .definition.abc import Definition


class ParseError(Exception):
    def __init__(self, t: typing.Type["Definition"], err: str = ""):
        self.t = t
        self.err = err

    def __repr__(self) -> str:
        return "(ParseError in {}: {})".format(self.t.__name__, self.err)
