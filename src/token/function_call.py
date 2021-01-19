from typing import List, Dict

from src.packages.graphics_package import GraphicsPackage
from src.packages.std_package import StdPackage
from src.token.token import Token, TokenType


class FunctionCall(Token):
    def eval(self, variables: Dict[str, any]):
        args = []
        for param in self.params:
            args.append(param.eval(variables))

        return self.eval_func(args, variables)

    def eval_func(self, args: list, variables: Dict[str, any]):
        name = self.name
        if name in GraphicsPackage.get_supported_functions():
            return GraphicsPackage.execute(name, variables, args)
        if name in StdPackage.get_supported_functions():
            return StdPackage.execute(name, variables, args)
        raise Exception(f"Unknown Function {name}")

    def __init__(self, name: str, params: List[Token]):
        super().__init__(TokenType.FUNC_CALL)
        self.params = params
        self.name = name
