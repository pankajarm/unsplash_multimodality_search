# client
TOP_K = 20
IMAGE_RESIZE_FACTOR = 2
DEBUG = False

# serving via REST
# HOST = "demo-cas.jina.ai"
HOST = "0.0.0.0"
PORT_EXPOSE = "51000"
PROTOCOL = 'grpc'
DATA_DA_FILE_NAME = 'unsplash_lite_da_20k.bin'
COMPRESSION_METHOD = 'lz4'