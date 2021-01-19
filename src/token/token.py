from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class TokenType(Enum):
    FUNC_DEF = 0  # function definition
    FUNC_CALL = 1  # function call
    DECLARATION = 2  # variable declaration
    IDENTIFIER = 3  # identifier
    LITERAL = 4  # literal
    ASSIGNMENT = 5  # assignment
    BIN_OP = 6  # binary operation
    UN_OP = 7  # Unary operation
    WHILE = 8  # while loop
    IF = 9  # conditional
    COMPOUND = 10  # list of tokens
    FOR = 11  # for loop


class LiteralType(Enum):
    AMP = 0  # Ampersand (Location)
    INT = 1  # integer
    STR = 2  # string
    LIST = 3  # list
    VOID = 4  # void


class Token(ABC):
    def __init__(self, token_type: TokenType):
        self.token_type = token_type

    def __str__(self):
        return self.token_type

    @abstractmethod
    def eval(self, variables: Dict[str, any]):
        pass
