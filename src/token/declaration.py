from token import Token, TokenType


class Declaration(Token):
    def __init__(self, identifier):
        super().__init__(TokenType.DECLARATION)
        self.identifier = identifier
