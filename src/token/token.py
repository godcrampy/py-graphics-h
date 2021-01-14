from enum import Enum


class TokenType(Enum):
    FUNC_DEF = 0  # function definition
    FUNC_CALL = 1  # function call
    DECLARATION = 2  # variable declaration [NOT USED, identifier used instead]
    IDENTIFIER = 3  # identifier
    LITERAL = 4  # literal


class LiteralType(Enum):
    AMP = 0  # Ampersand (Location)
    INT = 1  # integer
    STR = 2  # string


class Token:
    def __init__(self, token_type: TokenType):
        self.token_type = token_type

    def __str__(self):
        return self.token_type
