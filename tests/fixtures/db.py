import os
import pytest
from alembic.config import Config
from alembic import command
from app.dependencies.db import ConnectionFactory

os.environ['db_uri'] = os.environ['test_uri']  # set test uri as default for application


@pytest.fixture()
def db():
    """
    Initializes test DB and yields connection
    Then close connection and clear db
    :return: connection to test db
    """
    config = Config('/app/alembic.ini')
    command.upgrade(config, 'head')
    # alembic upgrade head
    connection = ConnectionFactory.get_connection()
    yield connection
    connection.close()
    # alembic downgrade base
    # In some cases clear everything via dropping tables is not possible
    # For example, when two tables have foreign keys on eachother
    # `table1` <---> `table2`
    # So dropping one of them will be raising errors in the constrait of the second,
    # and operation will not proceed overall
    # Considering downgrade scripts of migration are written properly we may just downgrade to the base.
    # Then, for example, constraint of one of the first table will be dropped before the second one drops
    # `table1` <---> `table2`  | `table1` <--- `table2` | `table1`
    command.downgrade(config, 'base')
