from tests.fixtures import *  # NoQA
# just to load all fixtures


def pytest_configure(config):  # NoQA
    from app.main import startup
    startup()
