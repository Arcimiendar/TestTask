from pydantic import BaseModel
from app.domain.calculation import OperationOptions, OperationCalculationMixin
from app.domain.db import SaveToDBOperationOutputMixin


class OperataionInput(BaseModel):
    left_operand: float
    right_operand: float


class Operation(OperationCalculationMixin, OperataionInput):
    operation: OperationOptions

    def calculate_output(self) -> 'OperationOutput':
        return OperationOutput(
            **self.dict(),
            result=self.calculate()
        )


class OperationOutput(SaveToDBOperationOutputMixin, Operation):
    result: float
