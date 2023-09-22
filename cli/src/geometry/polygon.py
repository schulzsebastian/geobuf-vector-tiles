def encode_polygon(feature_pbf, polygon, dimension, precision_factor):
    if len(polygon) > 1:
        feature_pbf.geometry.lengths.extend(len(points) for points in polygon)

    for points in polygon:
        cumulative_sum = [0] * dimension
        for point in points:
            deltas = [int(round(coord * precision_factor) - cumulative_sum[i]) for i, coord in enumerate(point)]
            feature_pbf.geometry.coords.extend(deltas)
            cumulative_sum = [cumulative_sum[i] + deltas[i] for i in range(dimension)]

def decode_polygon(feature_pbf, dimension, precision_factor):
    polygon, point = [], [0] * dimension
    
    for i in range(0, len(feature_pbf.geometry.coords), dimension):
        current_coords = [point[j] + feature_pbf.geometry.coords[i + j] for j in range(dimension)]
        polygon.append([float(coord) / precision_factor for coord in current_coords])
        point = current_coords
    
    return [polygon]
