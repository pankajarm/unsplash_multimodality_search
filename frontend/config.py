import os

# client
TOP_K = 10
IMAGE_RESIZE_FACTOR = 3
DEBUG = True

# serving via REST
# HOST = "demo-cas.jina.ai"
HOST = "0.0.0.0"
PORT_EXPOSE = "51000"
PROTOCOL = 'grpc'
DATA_DA_FILE_NAME = 'unsplash_lite_da_10k.bin'
COMPRESSION_METHOD = 'lz4'