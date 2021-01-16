from enum import Enum
from typing import Dict

from src.token.token import Token, TokenType


class BinaryOperator(Enum):
    ADD = "+"
    SUB = "-"
    MULT = "*"
    DIV = "/"


class BinaryOperation(Token):
    def eval(self, variables: Dict[str, any]):
        left_val = self.left.eval(variables)
        right_val = self.right.eval(variables)
        op = self.operator
        if op == BinaryOperator.ADD:
            return left_val + right_val
        if op == BinaryOperator.SUB:
            return left_val - right_val
        if op == BinaryOperator.MULT:
            return left_val * right_val
        if op == BinaryOperator.DIV:
            return left_val / right_val
        raise Exception("Unknown Operator in Binary Operation")

    def __init__(self, left: Token, right: Token, operator: BinaryOperator):
        super().__init__(TokenType.BIN_OP)
        self.left = left
        self.right = right
        self.operator = operator
