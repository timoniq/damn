from abc import ABC, abstractmethod


class Value(ABC):
    @abstractmethod
    def get_common_representation(self) -> str:
        pass

    @abstractmethod
    def get_formula_representation(self) -> str:
        pass

    @abstractmethod
    def cmp_to_user_input(self, s: str) -> bool:
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.get_common_representation()}>"
