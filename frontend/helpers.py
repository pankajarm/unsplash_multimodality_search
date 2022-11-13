import base64
from docarray import DocumentArray, Document
# from docarray.array.sqlite import SqliteConfig
from clip_client import Client
import urllib.request
from PIL import Image
import streamlit as st
from config import *

print("PROTOCOL:", PROTOCOL)
print("HOST:", HOST)
print("PORT_EXPOSE:", PORT_EXPOSE)

# load data da


def load_data_da(verbose=DEBUG):
    print("LOADING DATA DA.....")
    data_da = DocumentArray.load_binary(DATA_DA_FILE_NAME, compress=COMPRESSION_METHOD)
    print("SUCCESS.. data_da size:", len(data_da))
    if verbose:
        print(data_da.summary())
    return data_da

data_da = load_data_da(verbose=DEBUG)

# def get_docs_from_sqlite(connection: str, table: str) -> DocumentArray:
#     cfg = SqliteConfig(connection, table)
#     return DocumentArray(storage='sqlite', config=cfg)

def create_text_query_da(search_term: str) -> DocumentArray:
    return DocumentArray(Document(text=search_term))

# def create_image_query_da(img_path: str) -> DocumentArray:
#     return DocumentArray(Document(uri=img_path))

def get_client(show_progress: bool = DEBUG) -> Client:
    c = Client(server=PROTOCOL+'://'+HOST+':'+PORT_EXPOSE)
    c.show_progress = show_progress
    return c

def resize_image(filename: str, resize_factor: str=IMAGE_MAX_SIZE) -> Image:
    # w, h = image.size
    # return image.resize((w * resize_factor, h * resize_factor), Image.ANTIALIAS)
    print(filename)
    if "http" in filename:
        urllib.request.urlretrieve(filename, "test.png")
        image = Image.open("test.png")
        return image.thumbnail(IMAGE_MAX_SIZE)

def search_by_text(query_text:str, verbose=DEBUG):
    client = get_client()
    input_docarray = create_text_query_da(query_text)
    vec = client.encode(input_docarray, show_progress=DEBUG)
    results = data_da.find(query=vec, limit=TOP_K)
    if verbose:
        show_results_on_console(results,input_docarray)
    return results

def search_by_image(input, verbose=DEBUG):
    data = input.read()
    image_query_doc = Document(blob=data)
    image_query_doc.convert_blob_to_image_tensor()
    image_query_doc.set_image_tensor_shape((80, 60))

    client = get_client()
    # input_docarray = create_image_query_da(image_query_doc)
    input_docarray = DocumentArray(image_query_doc)
    vec = client.encode(input_docarray, show_progress=True)
    results = data_da.find(query=vec, limit=TOP_K)
    if verbose:
        show_results_on_console(results)
    return results

def show_results_on_console(results, query=None):
    if query:
        print(f"query_text: {query[0].text}")
    print(f"results are: {results}")
    for d in results[0]:
        print("d:", d)
        print(type(d))
        print(d.summary())
        print(d.uri, d.scores['cosine'].value) 
    return results