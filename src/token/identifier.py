from .token import Token, TokenType


class Identifier(Token):
    def __init__(self, name, value, literal_type):
        super().__init__(TokenType.IDENTIFIER)
        self.name = name
        self.value = value
        self.literal_type = literal_type
