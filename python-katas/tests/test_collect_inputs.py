import unittest
from assertpy import assert_that, fail

from onap_doc.blueprint_doc_generator import collect_inputs


class TestCollectInputs(unittest.TestCase):

    def test_all_attributes_have_descriptions(self):
        inputs = {'sdc_address': {'description': 'SDC host'}, 'sdc_uri': {'description': 'SDC url'}}
        data = collect_inputs(inputs)
        assert_that(data).is_equal_to({'sdc_address':'SDC host','sdc_uri': 'SDC url'})

    def test_not_all_attributes_have_descriptions(self):
        inputs = {'sdc_address': {'description': 'SDC host'}, 'sdc_uri': {}}
        data = collect_inputs(inputs)
        assert_that(data).is_equal_to({'sdc_address':'SDC host','sdc_uri': ''})





