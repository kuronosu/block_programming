from typing import Any
from .base import BaseBlock, Context, Reference, Response


class OperationBLock(BaseBlock):
    _name = "Operation"

    def _execute(self, context: Context) -> Response:
        ...


class BinaryOperationBLock(OperationBLock):
    _name = "BinaryOperation"
    _accepted_types = ()

    def __init__(self, value1: OperationBLock | Reference | Any, value2: OperationBLock | Reference | Any) -> None:
        self.value1 = value1
        self.value2 = value2

    def _get_values(self, context: Context) -> tuple:
        return (
            self._get_value(context, self.value1),
            self._get_value(context, self.value2)
        )

    def _get_value(self, context: Context, value) -> int | float:
        v = value
        if isinstance(value, Reference):
            if value.name not in context.variables:
                raise Exception(f"Variable {value} not found")
            v = context.variables[value.name]
        elif isinstance(value, OperationBLock):
            v = value._execute(context).value
        if not isinstance(v, self._accepted_types):
            raise Exception(
                f"Value '{v}' is not of type {self._accepted_types}")
        return v
