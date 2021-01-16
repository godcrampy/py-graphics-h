from typing import Dict

from src.token.token import Token, LiteralType, TokenType


class Declaration(Token):

    def eval(self, variables: Dict[str, any]):
        right_val = self.right.eval(variables)
        variables[self.name] = right_val

    def __init__(self, name: str, literal_type: LiteralType, right: Token):
        super().__init__(TokenType.DECLARATION)
        self.name = name
        self.literal_type = literal_type
        self.right = right
