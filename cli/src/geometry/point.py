def encode_point(feature_pbf, point, _, precision_factor):
    feature_pbf.geometry.coords.extend(int(round(coord * precision_factor)) for coord in point)

def decode_point(feature_pbf, _, precision_factor):
    return [float(coord) / precision_factor for coord in feature_pbf.geometry.coords]
