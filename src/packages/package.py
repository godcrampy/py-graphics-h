from abc import ABC, abstractmethod
from typing import List, Dict, Set


class Package(ABC):
    @classmethod
    @abstractmethod
    def get_supported_functions(cls) -> Set[str]:
        pass

    @classmethod
    @abstractmethod
    def execute(cls, name: str, variables: Dict[str, any], args: List):
        pass
