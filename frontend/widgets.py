import streamlit as st


def sidebar_widget():
    st.sidebar.title("Options")

    input_media = st.sidebar.radio(label="Search with...", options=["text", "image"])

    st.sidebar.markdown(
        """Image-to-Image and Text-to-Image Search using:
        [Jina](https://jina.ai)
        [Streamlit](https://streamlit.io)
        """
    )

    st.sidebar.markdown(
        "[Repo link](https://github.com/pankajarm/multi-modal-cloud-search)"
    )
    
    # st.sidebar.markdown(
    #     "[Credits](https://github.com/k-zehnder/jina-clip-streamlit)"
    # )
    return input_media

def paginator(label, items, image_ids, items_per_page=10, on_sidebar=True):
    """Lets the user paginate a set of items.

    Parameters
    ----------
    label : str
        The label to display over the pagination widget.
    items : Iterator[Any]
        The items to display in the paginator.
    items_per_page: int
        The number of items to display per page.
    on_sidebar: bool
        Whether to display the paginator widget on the sidebar.
        
    Returns
    -------
    Iterator[Tuple[int, Any]]
        An iterator over *only the items on that page*, including
        the item's index.
    """

    # Figure out where to display the paginator
    if on_sidebar:
        location = st.sidebar.empty()
    else:
        location = st.empty()

    # Display a pagination selectbox in the specified location.
    items = list(items)
    n_pages = len(items)
    n_pages = (len(items) - 1) // items_per_page + 1
    page_format_func = lambda i: "Page %s" % i
    page_number = location.selectbox(label, range(n_pages), format_func=page_format_func)

    # Iterate over the items in the page to let the user display them.
    min_index = page_number * items_per_page
    max_index = min_index + items_per_page
    import itertools
    return itertools.islice(enumerate(items), min_index, max_index)
    