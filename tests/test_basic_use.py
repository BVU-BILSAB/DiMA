from io import StringIO

import pytest
import json
from os.path import join, dirname
from itertools import product
from dima import Dima


@pytest.fixture
def test_input_data():
    return open(join(dirname(__file__), 'data/input.afa'), 'r').read()


@pytest.fixture
def test_basic_output_data():
    return json.load(open(join(dirname(__file__), 'data/basic_output.json'), 'r'))


@pytest.fixture
def test_advance_output_data():
    return json.load(open(join(dirname(__file__), 'data/advance_output.json'), 'r'))


def assert_all_properties(results, output_data):
    assert results.low_support_count == output_data.get('low_support_count')
    assert results.query_name == output_data.get('query_name')
    assert results.sequence_count == output_data.get('sequence_count')
    assert results.support_threshold == output_data.get('support_threshold')

    for new_position, old_position in zip(results.results, output_data.get('results')):
        assert new_position.position == old_position.get('position')
        assert new_position.support == old_position.get('support')
        assert new_position.low_support == old_position.get('low_support')
        assert new_position.distinct_variants_count == old_position.get('distinct_variants_count')
        assert round(new_position.total_variants_incidence) == round(old_position.get('total_variants_incidence'))
        assert round(new_position.distinct_variants_incidence) == round(old_position.get('distinct_variants_incidence'))

        if not new_position.diversity_motifs or not old_position.get('diversity_motifs'):
            continue

        for new_variant, old_variant in product(new_position.diversity_motifs, old_position.get('diversity_motifs')):
            if new_variant.sequence == old_variant.get('sequence'):
                assert new_variant.sequence == old_variant.get('sequence')
                assert new_variant.motif_long == old_variant.get('motif_long')
                assert new_variant.motif_short == old_variant.get('motif_short')
                assert round(new_variant.incidence) == round(old_variant.get('incidence'))
                assert new_variant.count == old_variant.get('count')

                if new_variant.metadata and old_variant.get('metadata'):
                    new_metadata, old_metadata = new_variant.metadata, old_variant.get('metadata')
                    keys = new_metadata.keys()
                    for key in keys:
                        assert new_metadata[key] == old_metadata[key]
                else:
                    assert new_variant.metadata == old_variant.get('metadata')


def test_module_basic_use(test_input_data, test_basic_output_data):
    results = Dima(sequences=StringIO(test_input_data)).run()

    assert_all_properties(results, test_basic_output_data)


def test_module_advance_use(test_input_data, test_advance_output_data):
    results = Dima(sequences=StringIO(test_input_data), header_format="accession|strain|country|date").run()

    assert_all_properties(results, test_advance_output_data)

