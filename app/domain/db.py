import psycopg2
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # for type hinting of mixins
    from app.domain.schema import OperationOutput   # it will not ever be evaluated on runtime
    Base = OperationOutput
else:
    Base = object


class SaveToDBOperationOutputMixin(Base):
    """
    Mixin for saving data to DB.
    """
    def save(self, conn: 'psycopg2.connection'):
        with conn.cursor() as curs:
            curs.execute("""
                INSERT INTO calculation_result(left_operand, right_operand, operation, result)
                VALUES (%(left_operand)s, %(right_operand)s, %(operation)s, %(result)s)
            """, self.dict())
            conn.commit()
