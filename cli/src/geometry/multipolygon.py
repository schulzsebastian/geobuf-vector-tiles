def populate_line(coords, line, closed, dimension, precision_factor):
    sum_ = [0] * dimension
    for point in line[:-1 if closed else len(line)]:
        coord = [round(coord * precision_factor) - sum_[i] for i, coord in enumerate(point)]
        coords.extend(coord)
        sum_ = [sum_[i] + coord[i] for i in range(dimension)]


def encode_multipolygon(feature_pbf, polygons, dimension, precision_factor):
    if len(polygons) != 1 or len(polygons[0]) != 1:
        lengths = [len(polygons)]
        for polygon in polygons:
            lengths.append(len(polygon))
            for inner_polygon in polygon:
                lengths.append(len(inner_polygon) - 1)
        feature_pbf.geometry.lengths.extend(lengths)
        
        coords = []
        for polygon in polygons:
            for inner_polygon in polygon:
                populate_line(coords, inner_polygon, True, dimension, precision_factor)
        feature_pbf.geometry.coords.extend(coords)
    else:
        for ring in polygons:
            for points in ring:
                cumulative_sum = [0] * dimension
                coords = []
                for point in points:
                    deltas = [int(round(coord * precision_factor) - cumulative_sum[i]) for i, coord in enumerate(point)]
                    coords.extend(deltas)
                    cumulative_sum = [cumulative_sum[i] + deltas[i] for i in range(dimension)]
                feature_pbf.geometry.coords.extend(coords)


def decode_multipolygon(feature_pbf, dimension, precision_factor):
    if len(feature_pbf.geometry.lengths) == 0:
        multipolygon = []
        point = [0] * dimension
        for i in range(0, len(feature_pbf.geometry.coords), dimension):
            _point = [point[j] + feature_pbf.geometry.coords[i + j] for j in range(dimension)]
            multipolygon.append([float(coord) / precision_factor for coord in _point])
            point = _point
        return [[multipolygon]]
    
    i = 0
    j = 1
    num_polygons = feature_pbf.geometry.lengths[0]
    multipolygons = []

    for _ in range(num_polygons):
        num_rings = feature_pbf.geometry.lengths[j]
        j += 1
        multipolygon = []
        for length in feature_pbf.geometry.lengths[j:j + num_rings]:
            coords = feature_pbf.geometry.coords[i:i + length * dimension]
            polygon = []
            point = [0] * dimension
            for coord in range(0, len(coords), dimension):
                _point = [point[p] + coords[coord + p] for p in range(dimension)]
                polygon.append([float(coord) / precision_factor for coord in _point])
                point = _point
            _point = [coords[p] for p in range(dimension)]
            polygon.append([float(coord) / precision_factor for coord in _point])
            multipolygon.append(polygon)
            j += 1
            i += length * dimension
        multipolygons.append(multipolygon)
    return multipolygons
