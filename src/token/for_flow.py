from typing import Dict

from src.token.token import Token, TokenType


class ForFlow(Token):
    def eval(self, variables: Dict[str, any]):
        self.init.eval(variables)
        while self.condition.eval(variables):
            self.stmt.eval(variables)
            self.next_op.eval(variables)
        return 0

    def __init__(self, init: Token, condition: Token, next_op: Token, stmt: Token):
        super().__init__(TokenType.FOR)
        self.condition = condition
        self.stmt = stmt
        self.next_op = next_op
        self.init = init
