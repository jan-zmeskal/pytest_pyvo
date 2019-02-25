import os
import pytest
import wget


from country_parser import CountryParser


@pytest.fixture(scope='module')
def json_dir(request):
    json_dir_name = 'test_data'
    os.mkdir(json_dir_name)

    def finalizer():
        os.rmdir(json_dir_name)

    request.addfinalizer(finalizer)

    return json_dir_name


@pytest.fixture(scope='module')
def json_files(json_dir, request):
    file_name = 'country-by-surface-area.json'
    url = 'https://raw.githubusercontent.com/samayo/country-json/master/src/'
    wget.download(url=url+file_name, out=json_dir, bar=None)

    def finalizer():
        os.remove(os.path.join(json_dir, file_name))

    request.addfinalizer(finalizer)


@pytest.fixture(scope='function')
def cp(json_dir, json_files):
    cp = CountryParser(data_dir=json_dir)
    cp.load_category(category='surface-area')
    return cp


def test_highest(cp):
    assert cp.highest().startswith('Russian Federation'), 'Russia must be the greatest!'


def test_lowest(cp):
    assert cp.lowest().startswith('Holy See'), 'Holy cow, Vatican is not the smallest!'


@pytest.mark.parametrize("test_input,expected", [
    ('Slovakia', 49012),
    ('Czech Republic', 78866),
    ('Germany', 357022)
])
def test_get(cp, test_input, expected):
    assert float(cp.get_value_for(test_input).split()[-1]) == expected
