from typing import Any

from .base import Context, Response
from .operation import OperationBLock


class AssignBlock(OperationBLock):
    def __init__(self, name: str, value: OperationBLock | Any) -> None:
        self.name = name
        self.value = value

    def _execute(self, context: Context) -> Response:
        context.variables[self.name] = self.value if not isinstance(
            self.value, OperationBLock) else self.value._execute(context).value
        return Response(context.variables[self.name])
