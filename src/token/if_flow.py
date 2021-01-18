from typing import Dict, List

from src.token.token import Token, TokenType, LiteralType


class IfFlow(Token):
    def eval(self, variables: Dict[str, any]):
        if self.condition.eval(variables):
            self.if_true.eval(variables)
        else:
            self.if_false.eval(variables)
        return 0

    def __init__(self, condition: Token, if_true: Token, if_false: Token):
        super().__init__(TokenType.IF)
        self.condition = condition
        self.if_true = if_true
        self.if_false = if_false

    def __str__(self):
        return f"IF({self.condition})"
