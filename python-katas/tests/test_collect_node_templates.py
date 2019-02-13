

import unittest
from assertpy import assert_that, fail

from onap_doc.blueprint_doc_generator import collect_inputs, collect_node_templates


class TestNodeTemplates(unittest.TestCase):


    def test_all_attributes_have_descriptions(self):
        attr_to_name = {
            'sdc_uri': 'SDC uri'
        }
        node_templates = {
            'service-change-handler': {
                'type': 'dcae.nodes.ContainerizedPlatformComponent',
                'properties': {
                    'name': 'service-change-handler',
                    'application_config': {
                        'asdcDistributionClient': {
                            'asdcAddress': {'get_input': 'sdc_address'},
                            'asdcUri': {'get_input': 'sdc_uri'},
                            'pollingTimeout': 20,
                            'consumerGroup': 'dcae'
                        }
                    }
                }
            }
        }

        data = collect_node_templates(node_templates, attr_to_name)
        assert_that(data).is_equal_to(
            {
                'service-change-handler':{
                    'asdcDistributionClient' : {
                        'asdcAddress' : '',
                        'asdcUri': 'SDC uri',
                        'pollingTimeout':'',
                        'consumerGroup':''
                    }
                }
            }
        )



