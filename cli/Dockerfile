FROM osgeo/gdal:ubuntu-small-latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install wget pip protobuf-compiler unzip build-essential libsqlite3-dev zlib1g-dev git sqlite3
RUN mkdir -p /tmp/tippecanoe-src
RUN git clone https://github.com/mapbox/tippecanoe.git /tmp/tippecanoe-src
RUN cd /tmp/tippecanoe-src && make && make install && rm -rf /tmp/tippecanoe-src
RUN mkdir -p /tmp/pmtiles
RUN cd /tmp/pmtiles && wget https://github.com/protomaps/go-pmtiles/releases/download/v1.10.0/go-pmtiles_1.10.0_Linux_x86_64.tar.gz && tar -xvf go-pmtiles_1.10.0_Linux_x86_64.tar.gz
RUN chmod +x /tmp/pmtiles/pmtiles && cp /tmp/pmtiles/pmtiles /usr/local/bin/pmtiles && rm -rf /tmp/pmtiles
RUN pip install msgspec protobuf==3.20.* psutil
WORKDIR /cli
CMD ["tail", "-f", "/dev/null"]