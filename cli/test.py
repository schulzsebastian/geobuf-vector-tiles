from src.geometry import encode_feature_collection, decode_feature_collection
from src import geobuf_pb2
import os

PRECISION_VALUE = int(os.getenv('PRECISION'))
DIMENSION = int(os.getenv('DIMENSION'))
PRECISION_FACTOR = pow(10, PRECISION_VALUE)
    
def test_feature_collection(feature_collection):
    pbf = geobuf_pb2.Data()
    encode_feature_collection(pbf, feature_collection, DIMENSION, PRECISION_FACTOR)
    geojson = decode_feature_collection(pbf, DIMENSION, PRECISION_FACTOR)
    for idx, feature_decoded in enumerate(geojson['features']):
        assert feature_decoded == feature_collection['features'][idx]

if __name__ == '__main__':
    test_feature_collection({
        'type': 'FeatureColelction',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [
                        16.932133,
                        52.408147
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': True,
                    'int': 1,
                    'neg_int': -1,
                    'float': 1.99,
                    'string': 'test'
                }
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [
                        16.932133,
                        52.408147
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': False,
                    'int': 1,
                    'neg_int': -1,
                    'float': -1.99,
                    'string': 'test'
                }
            }
        ]
    })
    test_feature_collection({
        'type': 'FeatureColelction',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'MultiPoint',
                    'coordinates': [
                        [
                            16.932133,
                            52.408147
                        ]
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': True,
                    'int': 1,
                    'neg_int': -1,
                    'float': 1.99,
                    'string': 'test'
                }
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'MultiPoint',
                    'coordinates': [
                        [
                            16.932133,
                            52.408147
                        ],
                        [
                            16.932133,
                            52.408147
                        ],
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': False,
                    'int': 1,
                    'neg_int': -1,
                    'float': -1.99,
                    'string': 'test'
                }
            }
        ]
    })
    test_feature_collection({
        'type': 'FeatureColelction',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'LineString',
                    'coordinates': [
                        [
                            16.754554,
                            52.311053
                        ],
                        [
                            17.090480,
                            52.495662
                        ]
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': True,
                    'int': 1,
                    'neg_int': -1,
                    'float': 1.99,
                    'string': 'test'
                }
            }
        ]
    })
    test_feature_collection({
        'type': 'FeatureColelction',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'MultiLineString',
                    'coordinates': [
                        [
                            [
                                16.754554,
                                52.311053
                            ],
                            [
                                17.090480,
                                52.495662
                            ]
                        ]
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': True,
                    'int': 1,
                    'neg_int': -1,
                    'float': 1.99,
                    'string': 'test'
                }
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'MultiLineString',
                    'coordinates': [
                        [
                            [
                                16.754554,
                                52.311053
                            ],
                            [
                                17.090480,
                                52.495662
                            ]
                        ],
                        [
                            [
                                16.754554,
                                52.311053
                            ],
                            [
                                17.090480,
                                52.495662
                            ]
                        ]
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': False,
                    'int': 1,
                    'neg_int': -1,
                    'float': -1.99,
                    'string': 'test'
                }
            }
        ]
    })
    test_feature_collection({
        'type': 'FeatureColelction',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [
                        [
                            [
                                16.753271,
                                52.495662
                            ],
                            [
                                16.753271,
                                52.311053
                            ],
                            [
                                17.090480,
                                52.311053
                            ],
                            [
                                17.090480,
                                52.495662
                            ],
                            [
                                16.753271,
                                52.495662
                            ]
                        ]
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': True,
                    'int': 1,
                    'neg_int': -1,
                    'float': 1.99,
                    'string': 'test'
                }
            }
        ]
    })
    test_feature_collection({
        'type': 'FeatureColelction',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'MultiPolygon',
                    'coordinates': [
                        [
                            [
                                [
                                    16.753271,
                                    52.495662
                                ],
                                [
                                    16.753271,
                                    52.311053
                                ],
                                [
                                    17.090480,
                                    52.311053
                                ],
                                [
                                    17.090480,
                                    52.495662
                                ],
                                [
                                    16.753271,
                                    52.495662
                                ]
                            ]
                        ]
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': True,
                    'int': 1,
                    'neg_int': -1,
                    'float': 1.99,
                    'string': 'test'
                }
            },
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'MultiPolygon',
                    'coordinates': [
                        [
                            [
                                [
                                    16.753271,
                                    52.495662
                                ],
                                [
                                    16.753271,
                                    52.311053
                                ],
                                [
                                    17.090480,
                                    52.311053
                                ],
                                [
                                    17.090480,
                                    52.495662
                                ],
                                [
                                    16.753271,
                                    52.495662
                                ]
                            ]
                        ],
                        [
                            [
                                [
                                    16.753271,
                                    52.495662
                                ],
                                [
                                    16.753271,
                                    52.311053
                                ],
                                [
                                    17.090480,
                                    52.311053
                                ],
                                [
                                    17.090480,
                                    52.495662
                                ],
                                [
                                    16.753271,
                                    52.495662
                                ]
                            ]
                        ]
                    ]
                },
                'properties': {
                    'id': 1,
                    'bool': False,
                    'int': 1,
                    'neg_int': -1,
                    'float': -1.99,
                    'string': 'test'
                }
            }
        ]
    })
    print('Test success')