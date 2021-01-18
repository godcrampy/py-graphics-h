from typing import Dict, List

from src.token.token import Token, TokenType, LiteralType


class WhileFlow(Token):
    def eval(self, variables: Dict[str, any]):
        while self.condition.eval(variables):
            for token in self.stmts:
                token.eval(variables)
        return 0

    def __init__(self, condition: Token, stmts: List[Token]):
        super().__init__(TokenType.WHILE)
        self.condition = condition
        self.stmts = stmts

    def __str__(self):
        return f"While({self.condition})"
