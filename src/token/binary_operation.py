from enum import Enum

from src.token.token import Token


class BinaryOperator(Enum):
    ADD = "+"
    SUB = "-"
    MULT = "*"
    DIV = "/"


class BinaryOperation(Token):
    def __init__(self, left: Token, right: Token, operator: BinaryOperator):
        self.left = left
        self.right = right
        self.operator = operator
