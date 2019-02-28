import pytest
import random
import time

@pytest.fixture(scope='function')
def cheap_fixture():
    print('Invoking cheap fixture')
    return random.randint(1, 10)

@pytest.fixture(scope='module')
def expensive_fixture():
    print('Invoking expensive fixture')
    time.sleep(3)
    return 'server is ready and running'

def test_ready(cheap_fixture, expensive_fixture):
    assert cheap_fixture > 0
    assert 'ready' in expensive_fixture

def test_running(cheap_fixture, expensive_fixture):
    assert cheap_fixture > 0
    assert 'ready' in expensive_fixture
