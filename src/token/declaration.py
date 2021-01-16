from src.token.token import Token, LiteralType


class Declaration(Token):

    def __init__(self, name: str, literal_type: LiteralType, right: Token):
        self.name = name
        self.literal_type = literal_type
        self.right = right
