from enum import Enum
from typing import Dict

from src.token.token import Token, TokenType


class BinaryOperator(Enum):
    ADD = "+"
    SUB = "-"
    MULT = "*"
    DIV = "/"
    EQ = "=="
    NEQ = "!="
    GEQ = ">="
    LEQ = "<="
    GT = ">"
    LT = "<"


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
        if op == BinaryOperator.EQ:
            return left_val == right_val
        if op == BinaryOperator.NEQ:
            return left_val != right_val
        if op == BinaryOperator.GEQ:
            return left_val >= right_val
        if op == BinaryOperator.LEQ:
            return left_val <= right_val
        if op == BinaryOperator.LT:
            return left_val < right_val
        if op == BinaryOperator.GT:
            return left_val > right_val
        raise Exception("Unknown Operator in Binary Operation")

    def __init__(self, left: Token, right: Token, operator: BinaryOperator):
        super().__init__(TokenType.BIN_OP)
        self.left = left
        self.right = right
        self.operator = operator
