from src.geometry import encode_feature_collection, decode_feature_collection
from msgspec.json import decode
from datetime import datetime
import src.geobuf_pb2 as geobuf_pb2
import subprocess
import logging
import psutil
import time
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

VOLUME_PATH = '/volume'
PRECISION_VALUE = int(os.getenv('PRECISION'))
DIMENSION = int(os.getenv('DIMENSION'))
PRECISION_FACTOR = pow(10, PRECISION_VALUE)

def check_geojson(data):
    features = data.get("features", [])
    count = len(features)
    assert count > 0
    logging.info(f"GeoJSON valid: {count} features")

def geojson_to_pbf(file_path):
    assert file_path.endswith('.geojson')
    with open(file_path, "rb") as f:
        geojson_data = decode(f.read())
    check_geojson(geojson_data)
    pbf = geobuf_pb2.Data()
    return encode_feature_collection(pbf, geojson_data, DIMENSION, PRECISION_FACTOR)

def generate_tiles_geobuf(layer_name, geobuf_path, log_path):
    process = psutil.Process(os.getpid())

    pmtiles_path = geobuf_path.split('.geobuf')[0] + '.pmtiles'

    start_main_time = time.time()
    print(f"[start][{process.memory_percent():3.1f}%] generate_tiles_geobuf")

    with open(log_path, "w") as log:
        log.write(f" ---- {datetime.now().isoformat()[:-3]} ---- \n")
        log.flush()
        subprocess.run([
            "tippecanoe",
            "-o",
            pmtiles_path,
            "--drop-densest-as-needed",
            "--drop-fraction-as-needed",
            "--drop-smallest-as-needed",
            "--no-feature-limit",
            "--no-tile-size-limit",
            "--minimum-zoom=8",
            "--maximum-zoom=16",
            "--base-zoom=14",
            "--low-detail=8",
            "--minimum-detail=12",
            "--full-detail=16",
            "--force",
            f"--name={layer_name}",
            f"--layer={layer_name}",
            str(geobuf_path),
        ], stdout=log, stderr=log, check=False)
        log.write(f" ---- {datetime.now().isoformat()[:-3]} generate_tiles_geobuf: {(time.time() - start_main_time):9.4f}s ---- \n")
        log.flush()

    print(f"[end][{process.memory_percent():3.1f}%] generate_tiles_geobuf: {(time.time() - start_main_time):9.4f}")
    return 

if __name__ == "__main__":
    layer_name = "power_lines_high"
    input_filename = layer_name + '.geojson'
    input_path = os.path.join(VOLUME_PATH, input_filename)
    output_path = os.path.join(VOLUME_PATH, input_filename.split('.geojson')[0] + '.geobuf')
    pbf = geojson_to_pbf(input_path)
    with open(output_path, "wb") as f:
        f.write(pbf.SerializeToString())
    logs_path = os.path.join(VOLUME_PATH, "logs.log")
    generate_tiles_geobuf(layer_name, output_path, logs_path)
