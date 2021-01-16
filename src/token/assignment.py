from enum import Enum
from typing import Dict

from src.token.identifier import Identifier
from src.token.token import Token, TokenType


class AssignmentOperator(Enum):
    EQ = "="
    PEQ = "+="
    SEQ = "-="
    MEQ = "*="
    DEQ = "/="


class Assignment(Token):
    def eval(self, variables: Dict[str, any]):
        right_val = self.right.eval(variables)
        op = self.operator
        if op == AssignmentOperator.EQ:
            variables[self.left.name] = right_val
        elif op == AssignmentOperator.PEQ:
            variables[self.left.name] += right_val
        elif op == AssignmentOperator.SEQ:
            variables[self.left.name] -= right_val
        elif op == AssignmentOperator.MEQ:
            variables[self.left.name] *= right_val
        elif op == AssignmentOperator.DEQ:
            variables[self.left.name] /= right_val
        return 0

    def __init__(self, left: Identifier, right: Token, operator: AssignmentOperator):
        super().__init__(TokenType.ASSIGNMENT)
        self.left = left
        self.right = right
        self.operator = operator
