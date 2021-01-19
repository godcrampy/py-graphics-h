from enum import Enum
from typing import Dict

from src.token.token import Token, TokenType


class UnaryOperator(Enum):
    AMP = "&"
    SUB = "-"
    PRE_INCR = "++"
    POST_INCR = "p++"
    PRE_DECR = "--"
    POST_DECR = "p--"


class UnaryOperation(Token):
    def eval(self, variables: Dict[str, any]):
        if self.operator == UnaryOperator.AMP:
            return self.token.eval(variables)
        if self.operator == UnaryOperator.SUB:
            return -1 * self.token.eval(variables)
        val = self.token.eval(variables)
        name = self.token.name
        if self.operator == UnaryOperator.PRE_INCR:
            variables[name] += 1
            return val + 1
        if self.operator == UnaryOperator.POST_INCR:
            variables[name] += 1
            return val
        if self.operator == UnaryOperator.PRE_DECR:
            variables[name] -= 1
            return val - 1
        if self.operator == UnaryOperator.POST_DECR:
            variables[name] -= 1
            return val
        raise Exception("Unknown Operator in Unary Operation")

    def __init__(self, token: Token, operator: UnaryOperator):
        super().__init__(TokenType.UN_OP)
        self.token = token
        self.operator = operator
