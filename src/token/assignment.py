from enum import Enum

from src.token.identifier import Identifier
from src.token.token import Token


class AssignmentOperator(Enum):
    EQ = "="
    PEQ = "+="
    SEQ = "-="
    MEQ = "*="
    DEQ = "/="


class Assignment(Token):
    def __init__(self, left: Identifier, right: Token, operator: AssignmentOperator):
        self.left = left
        self.right = right
        self.operator = operator
