import os
import pytest
import wget


from country_parser import CountryParser


@pytest.fixture()
def json_dir():
    json_dir_name = 'test_data'

    return json_dir_name


@pytest.fixture()
def json_files():
    file_name = 'country-by-surface-area.json'
    url = 'https://raw.githubusercontent.com/samayo/country-json/master/src/'


@pytest.fixture()
def cp():
    cp = None
    return cp


def test_highest():
    assert True


def test_lowest():
    assert True


def test_get():
    assert True
