from enum import Enum
from typing import Dict

from src.token.token import Token, TokenType


class UnaryOperator(Enum):
    AMP = "&"
    SUB = "-"


class UnaryOperation(Token):
    def eval(self, variables: Dict[str, any]):
        return self.token.eval(variables)

    def __init__(self, token: Token, operator: UnaryOperator):
        super().__init__(TokenType.UN_OP)
        self.token = token
        self.operator = operator
