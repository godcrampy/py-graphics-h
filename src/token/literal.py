from src.token.token import Token, TokenType, LiteralType


class Literal(Token):
    def __init__(self, value, literal_type: LiteralType):
        super().__init__(TokenType.LITERAL)
        self.value = value
        self.literal_type = literal_type

    def __str__(self):
        return f"Literal({self.value}, {self.literal_type})"
