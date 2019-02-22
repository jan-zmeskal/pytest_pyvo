import pytest


@pytest.fixture(scope='function')
def sample():
    return ['Harry', 'Ron', 'Hermione']


def test_length(sample):
    assert len(sample) == 3, 'We did not get three strings'


def test_type(sample):
    for element in sample:
        assert type(element) is str, '{} is not a string'.format(element)
