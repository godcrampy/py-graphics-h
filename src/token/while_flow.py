from typing import Dict

from src.token.token import Token, TokenType


class WhileFlow(Token):
    def eval(self, variables: Dict[str, any]):
        while self.condition.eval(variables):
            self.stmt.eval(variables)
        return 0

    def __init__(self, condition: Token, stmt: Token):
        super().__init__(TokenType.WHILE)
        self.condition = condition
        self.stmt = stmt
