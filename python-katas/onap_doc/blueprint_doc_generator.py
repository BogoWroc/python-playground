import yaml


def collect_inputs(data):
    ret = {}
    for key, value in data.items():
        ret[key] = value.get('description', '')

    return ret


def collect_node_templates(node_templates, attr_to_name):
    ret = {}

    for node_name, values in node_templates.items():
        properties = values['properties']
        if 'application_config' in properties:
            application_config = properties['application_config']
            ret[node_name] = {}
            for conf_element_name, attrs in application_config.items():

                attributes = {}
                ret[node_name][conf_element_name] = attributes
                for attr_name, attr_data in attrs.items():
                    if type(attr_data) is dict:
                        input_attr = attr_data.get('get_input', '')
                        attributes[attr_name] = attr_to_name.get(input_attr, '')
                    else:
                        attributes[attr_name] = ''

    return ret


def display_table_with_input_parameters(inputs):
    for name, desc in inputs.items():
        print('|{}|{}|'.format(name, desc))


def display_table_with_nodes(nodes):
    for node_name, elements in nodes.items():
        print(node_name)
        for element_name, attrs in elements.items():
            for attr_name, desc in attrs.items():
                print('|{}.{}|{}|'.format(element_name, attr_name, desc))


if __name__ == '__main__':
    with open("/home/bogumil/Developer/python-playground/python-katas/resources/blueprints/inventory.yaml-template",
              'r') as stream:
        try:
            data = yaml.load(stream)

            inputs = data['inputs']
            inputs_data = collect_inputs(inputs)
            node_templates = data['node_templates']
            display_table_with_input_parameters(inputs_data)
            print("")
            display_table_with_nodes(collect_node_templates(node_templates, inputs_data))
        except yaml.YAMLError as exc:
            print(exc)
