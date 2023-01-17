
from typing import Any, Optional


class Context:
    def __init__(self) -> None:
        self.variables = {}


class Response:
    def __init__(self, value: Any) -> None:
        self.value = value


class BaseBlock:
    def _execute(self, context: Context) -> Optional[Response]:
        ...


class Reference:
    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self) -> dict:
        return {
            "type": "Reference",
            "name": self.name
        }
