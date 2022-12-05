import streamlit as st
st.set_page_config(layout="wide")
from helpers import search_by_text, fetch_image_then_resize, search_by_image
from widgets import *
from config import IMAGE_MAX_SIZE, DEBUG

# Sidebar
input_media = sidebar_widget()
st.title("Unsplash lite Multimodal Search")

# functions
# get Results
def get_results_lists(results):
    matched_images = []
    captions_src_urls = []
    match_ids = []
    for match in results[0]:
        if "https://" in str(match.uri):
            image = fetch_image_then_resize(match.uri, resize_factor=IMAGE_MAX_SIZE)
            matched_images.append(image)
            src_url_link = f"{match.uri}"
            captions_src_urls.append(src_url_link)
            match_ids.append(match.id)
    st.balloons()
    return matched_images, captions_src_urls, match_ids

# Input Scren
if input_media == "text":
    text_query = st.text_input(label="Search term")
    if text_query:
        matches = search_by_text(text_query, verbose=DEBUG)
        if "show_paginator" not in st.session_state:
            st.session_state["show_paginator"] = True
        st.session_state["show_paginator"] = True

elif input_media == "image":
    image_query = st.file_uploader(label="Image file", type= ['png', 'jpg', 'jpeg', 'svg'] )
    if image_query:
        matches = search_by_image(image_query, verbose=DEBUG)
        if "show_paginator" not in st.session_state:
            st.session_state["show_paginator"] = True
        st.session_state["show_paginator"] = True
    else:
        st.info('☝️ Please Upload an Image file!')

def cb_save_current_image_to_session(image):
    image.save("input_recom.jpg")
    # st.session_state["show_paginator"] = False
    if "show_recommendations" not in st.session_state:
        st.session_state["show_recommendations"] = True
    st.session_state["show_recommendations"] = True
        
# show results
if "show_paginator" in st.session_state:
    if  st.session_state["show_paginator"]:
        if "matches" in locals():
            matched_images,captions_src_urls,match_ids = get_results_lists(matches)
            st.success("Your Search Results!")
            tab_labels = [ str(i) for i in range(len(match_ids))]
            for tab, image,src_url, match_id in zip(st.tabs(tab_labels), matched_images,captions_src_urls,match_ids):
                with tab:
                    tab.image(image, use_column_width="auto")
                    tab.markdown(f"Source ({src_url})")
                    similar_image_search_button = tab.button(label="Show Similar Images", key=match_id,  on_click=cb_save_current_image_to_session, args=(image,))
                    if similar_image_search_button:
                        similar_matches = search_by_image("input_recom.jpg", local_file=True, verbose=False)

                    ###TO-DO show recommendations
                    if "show_recommendations" in st.session_state:
                        if st.session_state["show_recommendations"]:
                            # show similar images
                            if "similar_matches" in locals():
                                sim_matched_images, sim_captions_src_urls, sim_matched_ids = get_results_lists(similar_matches)
                                tab.success("Found Similar Images!")
                                sim_tab_labels = [ str(i) for i in range(len(sim_matched_ids))]
                                for sim_tab, sim_image, sim_src_url, sim_match_id in zip(tab.tabs(sim_tab_labels), sim_matched_images, sim_captions_src_urls, sim_matched_ids):
                                    with sim_tab:
                                        sim_tab.image(sim_image, use_column_width="auto")
                                        sim_tab.markdown(f"Source ({sim_src_url})")
