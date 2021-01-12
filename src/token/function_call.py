from typing import List

from src.token.literal import Literal
from src.token.token import Token, TokenType


class FunctionCall(Token):
    def __init__(self, name: str, params: List[Literal]):
        super().__init__(TokenType.FUNC_CALL)
        self.params = params
        self.name = name
