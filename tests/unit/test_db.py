from psycopg2.extras import DictCursor
from app.domain.schema import OperationOutput, OperationOptions


def test_save_working(db):
    operation_output = OperationOutput(
        left_operand=1,
        right_operand=2,
        result=3,
        operation=OperationOptions.div
    )
    operation_output.save(db)
    with db.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute("""
            SELECT left_operand, right_operand, result, operation FROM calculation_result;
        """)
        selected_data = OperationOutput(**cursor.fetchone())

    assert operation_output == selected_data, 'Inserted and selected data are not equal!'
