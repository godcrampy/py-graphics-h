from typing import List

from src.token.literal import Literal
from src.token.token import Token, TokenType


class FunctionCall(Token):
    def __init__(self, name: str, params: List[Literal]):
        super().__init__(TokenType.FUNC_CALL)
        self.params = params
        self.name = name

    def __str__(self):
        return f"FunctionCall({self.name}, {[i.__str__() for i in self.params]})"
