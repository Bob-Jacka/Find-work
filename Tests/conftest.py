import pytest

from core.data.Config import Config


@pytest.fixture(scope="session")
def setup():
    config = Config()


@pytest.fixture(scope='session')
def teardown():
    pass
