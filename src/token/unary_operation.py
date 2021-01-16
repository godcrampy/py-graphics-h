from enum import Enum

from src.token.token import Token


class UnaryOperator(Enum):
    AMP = "&"
    SUB = "-"


class UnaryOperation(Token):
    def __init__(self, token: Token, operator: UnaryOperator):
        self.token = token
        self.operator = operator
