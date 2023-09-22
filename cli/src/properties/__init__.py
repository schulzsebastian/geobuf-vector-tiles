def encode_properties(properties_keys, properties_json, feature_pbf):
    for idx, key in enumerate(properties_keys):
        json_value = properties_json[key]
        value = feature_pbf.values.add()
        if isinstance(json_value, int):
            if json_value >= 0:
                value.pos_int_value = json_value
            else:
                value.neg_int_value = -json_value
        elif isinstance(json_value, float):
            value.double_value = json_value
        elif isinstance(json_value, bool):
            value.bool_value = json_value
        else:
            value.string_value = str(json_value)
        feature_pbf.properties.append(idx)
        feature_pbf.properties.append(len(feature_pbf.values) - 1)

def decode_properties(pbf, properties, values):
    properties_json = {}
    for i in range(0, len(properties), 2):
        key = pbf.keys[properties[i]]
        val = values[properties[i + 1]]
        value_type = val.WhichOneof('value_type')
        if value_type == 'string_value':
            properties_json[key] = val.string_value
        elif value_type == 'double_value':
            properties_json[key] = val.double_value
        elif value_type == 'pos_int_value':
            properties_json[key] = val.pos_int_value
        elif value_type == 'neg_int_value':
            properties_json[key] = -val.neg_int_value
        elif value_type == 'bool_value':
            properties_json[key] = val.bool_value
    return properties_json