import streamlit as st
from helpers import search_by_text, resize_image, search_by_image
from widgets import sidebar_widget, paginator


st.title("Unsplash lite Multimodal Search")

# ---------- Sidebar
input_media = sidebar_widget()
# ---------- Wait for user inputs
# ---------- Wait for user inputs
if input_media == "text":
    text_query = st.text_input(label="Search term")
    text_search_button = st.button("Search")
    if text_search_button:
        matches = search_by_text(text_query, verbose=False)
        st.success("success")

elif input_media == "image":
    image_query = st.file_uploader(label="Image file")
    image_search_button = st.button("Search")
    if image_search_button:
        matches = search_by_image(image_query, verbose=False)
        st.success("success")

# matched_images = []
if "matches" in locals():
    for match in matches[0]:
        # print("match:", match)
        # print("match.uri", match.uri)
        image = resize_image(match.uri, resize_factor=2)
        # matched_images.append(image)
        image_id = str(str(match.uri).split("/")[1]).split(".")[0]

        st.image(image, use_column_width="auto")
        st.markdown(f"Source (https://unsplash.com/photos/{image_id})")
        

    # image_iterator = paginator("Select a result page", matched_images,on_sidebar=False)
    # indices_on_page, images_on_page = map(list, zip(*image_iterator))
    # st.image(images_on_page, use_column_width="auto", caption=indices_on_page)