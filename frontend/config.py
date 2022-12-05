# client
TOP_K = 20
IMAGE_MAX_SIZE = (500,500)
DEBUG = False

# serving via REST
# HOST = "api.clip.jina.ai"
HOST = "0.0.0.0"

PORT_EXPOSE = "51000"
# PORT_EXPOSE = "2096"

PROTOCOL = 'grpc'
DATA_DA_FILE_NAME = 'unsplash_lite_img_emb_da.bin'
COMPRESSION_METHOD = 'lz4'
CLIP_TOKEN = '919c11b17c077c1bddf793db098ffe0f'