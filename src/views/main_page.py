import streamlit as st
from io import BytesIO
import base64
from PIL import Image
from streamlit_carousel import carousel
from streamlit import session_state as ss

if 'sidebar_state' not in ss:
    ss.sidebar_state = 'collapsed'
else :
    if 'sidebar_runs' in ss :
        pass
    else :
        ss.sidebar_state = 'expanded'
        ss.sidebar_runs = True

def open_close_sidebar():
    ss.sidebar_state = (
        "collapsed" if ss.sidebar_state == "expanded" else "expanded"
    )


def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def show_image(image_path):
    image_file = open(image_path, 'rb')
    image = Image.open(image_file)

    st.markdown(
        f"""
        <style>
            .rounded-image {{
                border-radius: 50%;
                overflow: hidden;
                width: 250px;
                margin: 0 auto;
                display: block;
            }}
        </style>
        <img src="data:image/png;base64, {image_to_base64(image)}" class="rounded-image">
        """,
        unsafe_allow_html=True,
    )

# Custom CSS for better styling
st.markdown("""
    <style>
    .main > div {
        padding-top: 4rem;
    }
    h1, h2, h3 {
        margin-bottom: 1rem;
    }
    .stButton>button {
        width: 100%;
        margin-bottom: 0.5rem;
    }
    .highlight {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
h3, h4, h5, h6 {
    color: #1F7A7A;
    margin-bottom: 0.5rem;
    sizing: border-box;
    padding: 10px;
    border-radius: 5px;
}

h1, h2 {
    color: #165555;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([3, 7], gap="large")

with col1:

    show_image('src/static/images/profile_picture.jpg')

    st.markdown("### Connect with me:")
    st.link_button(":material/mail: Email", "mailto:hossein.gmohammadi@gmail.com", use_container_width=True)
    st.link_button(":material/account_circle: LinkedIn", "https://www.linkedin.com/in/hossein-golmohammadi-gns/", use_container_width=True)
    st.link_button(":material/code: GitHub", "https://github.com/artmiss-gns", use_container_width=True)

    if st.button(":material/menu: Menu", use_container_width=True, type="primary"):
        open_close_sidebar()


    # st.info(
    #     "🚀 **New Feature Alert!** Check out my latest project on **Machine Learning Predictions**. Scroll down to explore!"
    # )
    # st.info("🚀 **New RAG API Project Launched** ([website](https://rag-ui.streamlit.app))")
    st.info("🎉 **IELTS Score Update!**\n\nProud to share I scored 8 overall! \n(R:9, L:8.5, S:7, W:7)")

with col2:
    st.title("Hossein Golmohammadi")
    st.subheader("Computer Science Student")

    st.markdown("""
    I'm a fourth-year Computer Science student at the University of Isfahan. My research interests include:
    - **Natural Language Processing**
    - **Natural Language Processing for Low-Recourced Languages**
    - **Information Retrieval**
    - **Sentiment Analysis and Opinion Mining**
    - **Computational Linguistics for Multilingual Systems**
    """
    )