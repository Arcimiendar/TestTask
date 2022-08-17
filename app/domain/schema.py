from pydantic import BaseModel
from app.domain.calculation import OperationOptions, OperationCalculationMixin
from app.domain.db import SaveToDBOperationOutputMixin


class OperataionInput(BaseModel):
    """
    Input model for user
    """
    left_operand: float
    right_operand: float


class Operation(OperationCalculationMixin, OperataionInput):
    """
    This class is used to contain ready for calculation data
    "Busyness logic" was added as mixin to the class to bind data and actions together.
    """
    operation: OperationOptions

    def calculate_output(self) -> 'OperationOutput':
        """
        perform calculation
        :return: ready for user output
        """
        return OperationOutput(
            **self.dict(),
            result=self.calculate()
        )


class OperationOutput(SaveToDBOperationOutputMixin, Operation):
    """
    Class for User output.
    Saving to DB was added as mixin.
    """
    result: float
