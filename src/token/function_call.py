from token import Token, TokenType


class FunctionCall(Token):
    def __init__(self, params):
        super().__init__(TokenType.FUNC_CALL)
        self.params = params
