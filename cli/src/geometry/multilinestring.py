from src.geometry.linestring import encode_linestring, decode_linestring

def encode_multilinestring(feature_pbf, lines, dimension, precision_factor):
    if len(lines) > 1:
        feature_pbf.geometry.lengths.extend(len(points) for points in lines)
    for points in lines:
        encode_linestring(feature_pbf, points, dimension, precision_factor)

def decode_multilinestring(feature_pbf, dimension, precision_factor):
    multilinestrings = []
    if not feature_pbf.geometry.lengths:
        return [decode_linestring(feature_pbf, dimension, precision_factor)]
    
    i = 0
    for idx in feature_pbf.geometry.lengths:
        end = i + idx * dimension
        segment_coords = feature_pbf.geometry.coords[i:end]
        
        multilinestring, point = [], [0] * dimension
        for k in range(0, len(segment_coords), dimension):
            current_coords = [point[j] + segment_coords[k + j] for j in range(dimension)]
            multilinestring.append([float(coord) / precision_factor for coord in current_coords])
            point = current_coords
        
        multilinestrings.append(multilinestring)
        i = end
    return multilinestrings
