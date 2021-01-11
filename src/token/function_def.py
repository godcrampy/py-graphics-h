from token import Token, TokenType


class FunctionDef(Token):
    def __init__(self, tokens):
        super().__init__(TokenType.FUNC_DEF)
        self.tokens = tokens
