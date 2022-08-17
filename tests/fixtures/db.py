import os
import pytest
from alembic.config import Config
from alembic import command
from app.dependencies.db import ConnectionFactory

os.environ['db_uri'] = os.environ['test_uri']


@pytest.fixture()
def db():
    config = Config('/app/alembic.ini')
    command.upgrade(config, 'head')
    # alembic init
    connection = ConnectionFactory.get_connection()
    yield connection
    connection.close()
    # alembic downgrade
    command.downgrade(config, 'base')


