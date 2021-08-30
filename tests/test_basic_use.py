import pytest
import json
from os.path import join, dirname
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


def _assert_all_properties(results, output_data):
    assert results.low_support == output_data.get('low_support')
    assert results.protein_name == output_data.get('protein_name')
    assert results.sequence_count == output_data.get('sequence_count')
    assert results.support_threshold == output_data.get('support_threshold')

    for new_position, old_position in zip(results.results, output_data.get('results')):
        assert new_position.position == old_position.get('position')
        assert new_position.support == old_position.get('support')
        assert new_position.low_support == old_position.get('low_support')
        assert new_position.distinct_variants_count == old_position.get('distinct_variants_count')
        assert round(new_position.distinct_variants_incidence) == round(old_position.get('distinct_variants_incidence'))

        new_entropy = new_position.entropy
        old_entropy = old_position.get('entropy')

        if new_entropy == 0 or old_entropy == 0:
            assert new_entropy == old_entropy
        else:
            assert (min(new_entropy, old_entropy) / max(new_entropy, old_entropy)) > 0.86

        if not new_position.variants or not old_position.get('variants'):
            continue

        for new_variant, old_variant in zip(sorted(new_position.variants, key=lambda x: x.count),
                                            sorted(old_position.get('variants'), key=lambda x: x['count'])):
            if (new_variant.motif_short == "I" and old_variant.get('motif_short') == "I") and (
                    new_variant.sequence != old_variant.get('sequence')):
                continue

            assert new_variant.sequence == old_variant.get('sequence')
            assert new_variant.motif_long == old_variant.get('motif_long')
            assert new_variant.motif_short == old_variant.get('motif_short')
            assert round(new_variant.incidence) == round(old_variant.get('incidence'))
            assert new_variant.count == old_variant.get('count')
            assert new_variant.metadata == old_variant.get('metadata')


def test_module_basic_use(test_input_data, test_basic_output_data):
    results = Dima(sequences=test_input_data, sequences_source='string').run()

    _assert_all_properties(results, test_basic_output_data)


def test_module_advance_use(test_input_data, test_advance_output_data):
    results = Dima(sequences=test_input_data, sequences_source='string', header_format="accession|strain|country|date")\
        .run()

    _assert_all_properties(results, test_advance_output_data)
