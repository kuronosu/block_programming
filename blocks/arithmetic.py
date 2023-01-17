from .base import Context, Response
from .operation import BinaryOperationBLock


class NumberBinaryOperationBLock(BinaryOperationBLock):
    _accepted_types = (int, float)


class SumBlock(NumberBinaryOperationBLock):
    _name = "Sum"

    def _execute(self, context: Context) -> Response:
        v1, v2 = self._get_values(context)
        return Response(v1 + v2)


class SubBlock(NumberBinaryOperationBLock):
    _name = "Sub"

    def _execute(self, context: Context) -> Response:
        v1, v2 = self._get_values(context)
        return Response(v1 - v2)


class MulBlock(NumberBinaryOperationBLock):
    _name = "Mul"

    def _execute(self, context: Context) -> Response:
        v1, v2 = self._get_values(context)
        return Response(v1 * v2)


class DivBlock(NumberBinaryOperationBLock):
    _name = "Div"

    def _execute(self, context: Context) -> Response:
        v1, v2 = self._get_values(context)
        return Response(v1 / v2)


class ModBlock(NumberBinaryOperationBLock):
    _name = "Mod"

    def _execute(self, context: Context) -> Response:
        v1, v2 = self._get_values(context)
        return Response(v1 % v2)


class PowBlock(NumberBinaryOperationBLock):
    _name = "Pow"

    def _execute(self, context: Context) -> Response:
        v1, v2 = self._get_values(context)
        return Response(v1 ** v2)
