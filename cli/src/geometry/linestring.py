def encode_linestring(feature_pbf, points, dimension, precision_factor):
    cumulative_sum = [0] * dimension
    for point in points:
        coords = [int(round(coord * precision_factor) - cumulative_sum[i]) for i, coord in enumerate(point)]
        feature_pbf.geometry.coords.extend(coords)
        cumulative_sum = [cumulative_sum[i] + coords[i] for i in range(dimension)]

def decode_linestring(feature_pbf, dimension, precision_factor):
    coords = feature_pbf.geometry.coords
    decoded_points, cumulative_coords = [], [0] * dimension
    
    for i in range(0, len(coords), dimension):
        current_coords = [cumulative_coords[j] + coords[i + j] for j in range(dimension)]
        decoded_points.append([float(coord) / precision_factor for coord in current_coords])
        cumulative_coords = current_coords
        
    return decoded_points
