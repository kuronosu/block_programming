
from typing import Any, Optional
from .base import BaseBlock, Context, Reference, Response
from .operation import OperationBLock


class PrintBlock(BaseBlock):
    def __init__(self, *val: Reference | OperationBLock | Any, **kwargs) -> None:
        self.val = val
        self.kwargs = kwargs

    def _execute(self, context: Context) -> Optional[Response]:
        res = []
        for v in self.val:
            if isinstance(v, OperationBLock):
                res.append(v._execute(context).value)
            elif isinstance(v, Reference):
                res.append(context.variables[v.name])
            else:
                res.append(v)
        print(*res, **self.kwargs)


class InputBlock(OperationBLock):
    def __init__(self, msg: str) -> None:
        self.msg = msg

    def _execute(self, context: Context) -> Response:
        return Response(input(self.msg))


class ParseBlock(OperationBLock):
    def __init__(self, t: Any, val: Reference | OperationBLock | Any) -> None:
        self.val = val
        self.t = t

    def _execute(self, context: Context) -> Response:
        if isinstance(self.val, OperationBLock):
            return Response(self.t(self.val._execute(context).value))
        elif isinstance(self.val, Reference):
            return Response(self.t(context.variables[self.val.name]))
        return Response(self.t(self.val))
