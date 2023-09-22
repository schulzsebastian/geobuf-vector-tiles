FROM osgeo/gdal:ubuntu-small-latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install pip protobuf-compiler unzip build-essential libsqlite3-dev zlib1g-dev git sqlite3
RUN mkdir -p /tmp/tippecanoe-src
RUN git clone https://github.com/mapbox/tippecanoe.git /tmp/tippecanoe-src
RUN cd /tmp/tippecanoe-src && make && make install && rm -rf /tmp/tippecanoe-src
RUN pip install msgspec protobuf==3.20.* psutil
WORKDIR /cli
CMD ["tail", "-f", "/dev/null"]