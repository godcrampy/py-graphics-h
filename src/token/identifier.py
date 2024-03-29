from typing import Dict

from .token import Token, TokenType, LiteralType


class Identifier(Token):
    def eval(self, variables: Dict[str, any]):
        return variables[self.name]

    def __init__(self, name: str, value, literal_type: LiteralType):
        super().__init__(TokenType.IDENTIFIER)
        self.name = name
        self.value = value
        self.literal_type = literal_type