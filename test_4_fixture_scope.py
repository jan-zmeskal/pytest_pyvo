import pytest
import random
import time


@pytest.fixture(scope='function')
def cheap_fixture():
    print('\nInvoking cheap fixture')
    return random.randint(1, 10)


@pytest.fixture(scope='module')
def expensive_fixture():
    print('\nInvoking expensive fixture')
    time.sleep(3)
    return 'Server is ready and running'


def test_ready(cheap_fixture, expensive_fixture):
    assert cheap_fixture > 0
    assert 'ready' in expensive_fixture


def test_running(cheap_fixture, expensive_fixture):
    assert cheap_fixture > 0
    assert 'running' in expensive_fixture
