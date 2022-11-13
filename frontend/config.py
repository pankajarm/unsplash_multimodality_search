# client
TOP_K = 20
IMAGE_RESIZE_FACTOR = 1
DEBUG = False

# serving via REST
# HOST = "demo-cas.jina.ai"
HOST = "0.0.0.0"
PORT_EXPOSE = "51000"
PROTOCOL = 'grpc'
DATA_DA_FILE_NAME = 'src_uri_unsplash_lite_emb_da.bin'
COMPRESSION_METHOD = 'lz4'