from typing import Dict, List

from src.token.token import Token, TokenType


class Compound(Token):
    def eval(self, variables: Dict[str, any]):
        for token in self.tokens:
            token.eval(variables)
        return 0

    def __init__(self, tokens: List[Token]):
        super().__init__(TokenType.WHILE)
        self.tokens = tokens
