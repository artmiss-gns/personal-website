import streamlit as st
from streamlit import session_state as ss
from io import BytesIO
import base64

if 'sidebar_state' not in ss:
    ss.sidebar_state = 'collapsed'

st.set_page_config(
    initial_sidebar_state=ss.sidebar_state,
    page_title="Hossein Golmohammadi - CS Student",
    page_icon="🖥️",
    layout="wide",
)


def change():
    ss.sidebar_state = (
        "collapsed" if ss.sidebar_state == "expanded" else "expanded"
    )

# Page setup 
main_page = st.Page(
    page='views/main_page.py',
    title='Main Page',
    icon=':material/home:',
    url_path='/',
    default=True
)
projects = st.Page(
    page='views/projects.py',
    title='Projects',
    icon=':material/folder:',
    url_path='/projects',
)

extracurricular = st.Page(
    page='views/extracurricular.py',
    title='Extracurricular',
    icon=':material/book:',
    url_path='/extracurricular',
)

certificates = st.Page(
    page='views/certificates.py',
    title='Certificates',
    icon=':material/book:',
    url_path='/certificates',
)

skills = st.Page(
    page='views/skills.py',
    title='Skills',
    icon=':material/construction:',
    url_path='/skills',
)

education = st.Page(
    page='views/education.py',
    title='Education',
    icon=':material/school:',
    url_path='/education',
)

# Navigation bar
nav = st.navigation(pages=[main_page, ])
pg = st.navigation(
    {
        "": [main_page],
        "About": [education, skills, certificates],

        "Projects": [projects],
        "Other": [extracurricular],
    }
)

# download CV from sidebar
# cv_buffer = BytesIO() # Create a buffer to hold the CV file
# with open('src/static/cv.pdf', 'rb') as cv_file:
#     cv_buffer.write(cv_file.read())

# cv_button = st.sidebar.download_button(
#     label="Download CV",
#     data=cv_buffer.getvalue(),
#     file_name="Hossein-Golmohammadi_cv.pdf",
#     mime="application/pdf",
#     key="download_cv",
# )

# selected = option_menu(
#     menu_title=None,
#     options=["Info", "Projects", "Extracurricular"],
#     icons=["house", "book", "envelope"],
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal",
#     # styles={
#     #     "container": {"padding": "0px", "background-color": "#ffffff"},
#     #     "icon": {"color": "#666", "font-size": "20px"},
#     #     "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px"},
#     #     "nav-link-selected": {"background-color": "#f0f0f0", "color": "#333"},
#     # }
# )


st.logo(
    'src/static/logos/logo.png',
    link='https://github.com/artmiss-gns',
)
# st.sidebar.text("Made by Hossein :)")
pg.run()