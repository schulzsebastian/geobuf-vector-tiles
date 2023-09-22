from src.geometry.point import encode_point, decode_point
from src.geometry.multipoint import encode_multipoint, decode_multipoint
from src.geometry.linestring import encode_linestring, decode_linestring
from src.geometry.multilinestring import encode_multilinestring, decode_multilinestring
from src.geometry.polygon import encode_polygon, decode_polygon
from src.geometry.multipolygon import encode_multipolygon, decode_multipolygon
from src.properties import encode_properties, decode_properties

GEOMETRY_TYPES_STR_TO_INT = {
    'Point': 0,
    'MultiPoint': 1,
    'LineString': 2,
    'MultiLineString': 3,
    'Polygon': 4,
    'MultiPolygon': 5
}
GEOMETRY_TYPES_INT_TO_STR = {v: k for k, v in GEOMETRY_TYPES_STR_TO_INT.items()}

ENCODE_GEOMETRY_FUNCTIONS = {
    'Point': encode_point,
    'MultiPoint': encode_multipoint,
    'LineString': encode_linestring,
    'MultiLineString': encode_multilinestring,
    'Polygon': encode_polygon,
    'MultiPolygon': encode_multipolygon
}

DECODE_GEOMETRY_FUNCTIONS = {
    'Point': decode_point,
    'MultiPoint': decode_multipoint,
    'LineString': decode_linestring,
    'MultiLineString': decode_multilinestring,
    'Polygon': decode_polygon,
    'MultiPolygon': decode_multipolygon
}

def encode_feature(geometry_json, feature_pbf, dimension, precision_factor):
    feature_pbf.geometry.type = GEOMETRY_TYPES_STR_TO_INT[geometry_json['type']]
    ENCODE_GEOMETRY_FUNCTIONS[geometry_json['type']](feature_pbf, geometry_json['coordinates'], dimension, precision_factor)

def encode_feature_collection(pbf, geojson_data, dimension, precision_factor):
    properties_keys = list(geojson_data['features'][0]['properties'].keys())
    for key in properties_keys:
        pbf.keys.append(key)
    for feature_json in geojson_data['features']:
        feature = pbf.feature_collection.features.add()
        encode_feature(feature_json['geometry'], feature, dimension, precision_factor)
        encode_properties(properties_keys, feature_json['properties'], feature)
    return pbf

def decode_feature_collection(pbf, dimension, precision_factor):
    feature_collection = {'type': 'FeatureCollection', 'features': []}
    for feature in pbf.feature_collection.features:
        feature_collection['features'].append({
            'type': 'Feature',
            'geometry':{
                'type': GEOMETRY_TYPES_INT_TO_STR[feature.geometry.type],
                'coordinates': DECODE_GEOMETRY_FUNCTIONS[GEOMETRY_TYPES_INT_TO_STR[feature.geometry.type]](
                    feature,
                    dimension,
                    precision_factor
                )
            },
            'properties': decode_properties(pbf, feature.properties, feature.values)
        })
    return feature_collection