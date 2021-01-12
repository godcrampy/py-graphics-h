from .token import Token, TokenType, LiteralType


class Identifier(Token):
    def __init__(self, name: str, value, literal_type: LiteralType):
        super().__init__(TokenType.IDENTIFIER)
        self.name = name
        self.value = value
        self.literal_type = literal_type

    def __str__(self):
        return f"Identifier({self.name}, {self.value})"
