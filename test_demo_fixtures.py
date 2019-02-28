import pytest

@pytest.fixture()
def sample():
    return ['Harry', 'Ron', 'Hermione']

def test_length(sample):
    assert len(sample) == 3

def test_type(sample):
    for element in sample:
        assert type(element) is str
