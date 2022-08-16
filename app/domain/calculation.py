from enum import Enum
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domain.schema import Operation
    Base = Operation
else:
    Base = object


class OperationOptions(str, Enum):
    add = '+'
    sub = '-'
    div = '/'
    mul = '*'


functors = {
    OperationOptions.add: lambda r, l: r + l,
    OperationOptions.mul: lambda r, l: r * l,
    OperationOptions.div: lambda r, l: r / l,
    OperationOptions.sub: lambda r, l: r - l,
}


class OperationCalculationMixin(Base):

    def calculate(self) -> float:
        return functors[self.operation](self.left_operand, self.right_operand)

