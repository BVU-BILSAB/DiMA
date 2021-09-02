import json
import pytest

from io import StringIO
from os.path import join, dirname
from .test_basic_use import assert_all_properties
from dima import Dima


@pytest.fixture
def test_input_data():
    return open(join(dirname(__file__), 'data/input_incons_headers.afa'), 'r').read()


@pytest.fixture
def test_incons_headers_output_data():
    return json.load(open(join(dirname(__file__), 'data/incons_input_results.json'), 'r'))


def test_incons_headers_use(test_input_data, test_incons_headers_output_data):
    results = Dima(StringIO(test_input_data), header_format="accession|strain|species|date",
                   header_fillna="Not Given").run()

    assert_all_properties(results, test_incons_headers_output_data)
