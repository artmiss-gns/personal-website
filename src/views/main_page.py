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

    show_image('src/static/images/profile_picture.webp')

    st.markdown("### Connect with me:")
    st.link_button(":material/mail: Email", "mailto:hossein.gmohammadi@gmail.com", use_container_width=True)
    st.link_button(":material/account_circle: LinkedIn", "https://www.linkedin.com/in/hossein-golmohammadi-gns/", use_container_width=True)
    st.link_button(":material/code: GitHub", "https://github.com/artmiss-gns", use_container_width=True)

    cv_buffer = BytesIO() # Create a buffer to hold the CV file
    with open('src/static/cv.pdf', 'rb') as cv_file:
        cv_buffer.write(cv_file.read())

    cv_button = st.download_button(
        label=":material/description: Download CV",
        data=cv_buffer.getvalue(),
        file_name="Hossein-Golmohammadi_cv.pdf",
        mime="application/pdf",
        use_container_width=True
    )

    if st.button(":material/menu: Menu", use_container_width=True, type="primary"):
        open_close_sidebar()


with col2:
    st.title("Hossein Golmohammadi")
    st.subheader("Computer Science Student | Machine Learning Enthusiast")
    
    # st.markdown("""
    # I'm a fourth-year Computer Science student at the University of Isfahan, specializing in Machine Learning and ranked in the<br>
    # **top 10%** of my class.<br>
    # My research interests include **Natural Language Processing**, **Information Retrieval**, and **Adversarial Machine Learning**.<br>
    # I'm also passionate about **DevOps** and **MLOps**, focusing on streamlining the deployment and management of ML models in production environments.<br>
    # I'm passionate about advancing AI and data science through innovative research and practical applications.
    # """, unsafe_allow_html=True)

    st.markdown("""
    I'm a fourth-year Computer Science student at the University of Isfahan, specializing in Machine Learning and ranked in the top 10% of my class. My research interests include:
    - **Natural Language Processing**  
    - **Information Retrieval**  
    - **Adversarial Machine Learning**  
    - **Computer Vision**  
    - **Machine Learning Operations (MLOps)**  

    I'm passionate about advancing AI and data science through innovative research and practical applications. My focus extends to DevOps and MLOps practices, aiming to streamline the deployment and management of ML models in production environments.
    """)
    st.markdown("""
        ### Highlights
        - 🏆 Ranked in top 10% of Computer Science class
        - 🐍 4+ years of Python expertise with focus on ML frameworks
        - 🧠 Strong foundation in ML theory and hands-on experience in predictive modeling
        - 👨‍🏫 Teaching Assistant for Algorithms and Data Structures course
        - 🚀 Developed multiple ML projects including RAG systems and predictive models
        - 🔧 Experienced in DevOps practices and cloud deployment (AWS, Docker)
        - 🔍 Aspiring AI researcher with a focus on NLP and Information Retrieval
    """, unsafe_allow_html=True)


# st.markdown("---")

# Featured Projects Gallery
# st.header("Featured Projects")

# # Define your project cards
# project_cards = [
#     {
#         "title": "RAG System with Embedded Knowledge Base",
#         "text": "Developed a Retrieval-Augmented Generation system using PDF-based knowledge base with heavy preprocessing and LLM integration.",
#         "img": "src/static/images/img1.webp",
#         "link": "https://github.com/artmiss-gns/rag-project"
#     },
#     {
#         "title": "Stock Market Prediction using LSTM",
#         "text": "Implemented an LSTM-based model for stock price prediction using PyTorch with custom data preprocessing pipeline.",
#         "img": "src/static/images/img2.webp",
#         "link": "https://github.com/artmiss-gns/Stock-Market-Prediction-using-LSTM"
#     },
#     {
#         "title": "Chronic Kidney Disease Prediction Model",
#         "text": "Developed and compared 7 ML models achieving 99% accuracy with XGBoost and Random Forest for kidney disease prediction.",
#         "img": "src/static/images/img3.webp",
#         "link": "https://github.com/artmiss-gns/kidney-disease-prediction"
#     },
#     # Add more project cards as needed
# ]

# # Create the carousel
# c1, c2, c3 = st.columns([1, 4, 1])
# with c2:
#     carousel(items=project_cards, container_height=900, width=70)
