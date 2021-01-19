from typing import Dict, List, Set

from src.packages.package import Package


class StdPackage(Package):
    @classmethod
    def get_supported_functions(cls) -> Set[str]:
        return {"snprintf", "printf"}
        pass

    @classmethod
    def execute(cls, name: str, variables: Dict[str, any], args: List):
        if name == "printf":
            print(args[0])
            return 0
        if name == "snprintf":
            format_str: str = args[2]
            format_str = format_str.replace("%d", "{}").format(*args[3:])
            variables['buf'] = format_str
            return 0
        raise Exception(f"Function {name} not in Standard Package")
