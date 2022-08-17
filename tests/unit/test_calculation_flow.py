from app.domain.schema import OperationOutput, OperationOptions, Operation


def test_calculation_flow_works():
    operation = Operation(
        left_operand=1,
        right_operand=2,
        operation=OperationOptions.add
    )
    expected_output = OperationOutput(
        **operation.dict(),
        result=3,
    )
    real_output = operation.calculate_output()

    assert real_output == expected_output
