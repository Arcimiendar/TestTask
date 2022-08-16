from enum import Enum
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domain.schema import Operation
    Base = Operation
else:
    Base = object


class MathError(ValueError):
    def __init__(self, *args, detailed: str):
        self.detailed = detailed
        super(MathError, self).__init__(*args)


class OperationOptions(str, Enum):
    add = '+'
    sub = '-'
    div = '/'
    mul = '*'


def div(left: float, right: float) -> float:
    if right == 0:
        raise MathError('Divizion by 0', detailed='right operand equals to 0 (may be 0, +0, -0)')
    return left / right


functors = {
    OperationOptions.add: lambda l, r: l + r,
    OperationOptions.mul: lambda l, r: l * r,
    OperationOptions.div: div,
    OperationOptions.sub: lambda l, r: l - r,
}


class OperationCalculationMixin(Base):

    def calculate(self) -> float:
        return functors[self.operation](self.left_operand, self.right_operand)
