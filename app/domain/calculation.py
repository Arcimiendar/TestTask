from enum import Enum
from typing import TYPE_CHECKING


if TYPE_CHECKING:  # for type hinting of mixins
    from app.domain.schema import Operation  # it will not be evaluated on runtime
    Base = Operation
else:
    Base = object


class MathError(ValueError):
    """
    This exception is used for "math" errors such as division by zero
    """
    def __init__(self, *args, detailed: str):
        self.detailed = detailed
        super(MathError, self).__init__(*args)


class OperationOptions(str, Enum):
    """
    Available operations
    """
    add = '+'
    sub = '-'
    div = '/'
    mul = '*'


def div(left: float, right: float) -> float:
    """
    functor for devisiom
    :raises MathError if right operand is 0
    :param left: left operand
    :param right: right operand
    :return: result of division left operand by right operand
    """
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
    """
    Mixin for calculation.
    Separated from original class for code decomposition
    """

    def calculate(self) -> float:
        """
        perform "Busyness logic" of computation
        :return: result computation
        """
        return functors[self.operation](self.left_operand, self.right_operand)
