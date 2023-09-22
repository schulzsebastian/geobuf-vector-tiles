## Geobuf Vector Tiles (experimental)

1. Msgspec Python JSON parser
2. Custom Geobuf converter
3. Tippecanoe / PMTiles

## Usage

1. Run stack

```
docker-compose up --build -d
```

2. Run tests

```
docker exec -i geobuf-cli python test.py
```

3. Put `<layer_name>.geojson` in `./volume` and change `layer_name` in `cli.py`.

4. Run script

```
docker exec -it geobuf-cli python cli.py
```
