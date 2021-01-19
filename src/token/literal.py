from typing import Dict

from src.token.token import Token, TokenType, LiteralType


class Literal(Token):
    def eval(self, variables: Dict[str, any]):
        if self.literal_type == LiteralType.LIST:
            vals = []
            for lit in self.value:
                vals.append(lit.eval(variables))
            return vals
        return self.value

    def __init__(self, value, literal_type: LiteralType):
        super().__init__(TokenType.LITERAL)
        self.value = value
        self.literal_type = literal_type
