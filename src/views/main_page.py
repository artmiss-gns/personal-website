import streamlit as st
from io import BytesIO
import base64
from PIL import Image



def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def show_image(image_path):
    image_file = open('src/static/images/profile_picture.webp', 'rb')
    image = Image.open(image_file)

    # Display the image with a rounded corner style
    st.markdown(
        f"""
        <style>
            .rounded-image {{
                border-radius: 50%;
                overflow: hidden;
                width: 300px;
            }}
        </style>
        <img src="data:image/png;base64, {image_to_base64(image)}" class="rounded-image">
        """,
        unsafe_allow_html=True,
    )

# download CV from sidebar

cv_buffer = BytesIO() # Create a buffer to hold the CV file
with open('src/static/cv.pdf', 'rb') as cv_file:
    cv_buffer.write(cv_file.read())

cv_button = st.sidebar.download_button(
    label="Download CV",
    data=cv_buffer.getvalue(),
    file_name="Hossein-Golmohammadi_cv.pdf",
    mime="application/pdf",
    key="download_cv",
)

# Hero Section
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    show_image(image_path='src/static/images/profile_picture.webp')

with col2:
    st.title("Hi, I'm artmiss", anchor=False)
    st.write("I'm a Data Scientist with a passion for leveraging data to drive insights and solve complex problems.")
    st.write("I specialize in machine learning, data analysis, and visualization.")
    st.write("Let's connect and explore how we can collaborate on exciting projects!")

    st.link_button(":material/mail: Contact me", "mailto:artmiss.gns@gmail.com")

# Highlights
st.write("---")
st.subheader("Highlights")
st.write("""
    I am a highly skilled Data Scientist with a strong background in machine learning, data analysis, and visualization.
    I have a proven track record of delivering valuable insights and solutions to complex problems.
    I am passionate about leveraging data to drive business growth and improve decision-making.
""")

# Skills
st.write("---")
st.subheader("Skills")
st.write("""
- **Programming Languages:** Python, R, SQL
- **Data Analysis:** Pandas, NumPy, Matplotlib, Seaborn, Plotly
- **Machine Learning:** Scikit-learn, TensorFlow, PyTorch
- **Data Visualization:** Tableau, Power BI, Matplotlib, Seaborn, Plotly
- **Cloud Platforms:** AWS, Google Cloud Platform (GCP)
- **Version Control:** Git, GitHub
- **Databases:** MySQL, PostgreSQL, MongoDB
- **Tools:** Jupyter Notebook, Anaconda, Docker, Flask, Streamlit
""")



# Add some styling to make it look cool
st.markdown("""
<style>
    #download_cv {
        background-color: #4CAF50;
        color: #FFFFFF;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    #download_cv:hover {
        background-color: #3e8e41;
    }
</style>
""", unsafe_allow_html=True)