from token import Token, TokenType


class Literal(Token):
    def __init__(self, value, literal_type):
        super().__init__(TokenType.LITERAL)
        self.value = value
        self.literal_type = literal_type
