import streamlit as st

# Define color palette
primaryColor = "#279095"
backgroundColor = "#eff3f9"
secondaryBackgroundColor = "#D1D6DC"
textColor = "#333333"
font = "sans serif"

# Apply background color to the entire page
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {backgroundColor};
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(f"""
<style>
    body {{
        color: {textColor};
    }}
    .container {{
        max-width: 800px;
        margin: 0 auto;
        padding: 1rem;
    }}
    h1 {{
        color: {primaryColor};
        font-size: 35px;
        margin-bottom: 20px;
        text-align: center;
        border-bottom: 2px solid {primaryColor};
        padding-bottom: 10px;
        margin-left: 5rem;
        margin-right: 5rem;
    }}
    h2 {{
        color: {primaryColor};
        font-size: 30px;
        margin-top: 25px;
        margin-bottom: 15px;
    }}
    h3 {{
        color: {textColor};
        font-size: 20px;
        margin-top: 5px;
        margin-bottom: 5px;
        margin-left: 3rem;
        margin-right: 3rem;
    }}
    .skill-item {{
        background-color: {primaryColor};
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        margin: 5px;
        display: inline-block;
        font-size: 14px;
        transition: all 0.3s ease;
    }}
    .skill-item:hover {{
        background-color: {secondaryBackgroundColor};
        color: {textColor};
    }}
    .subcategory {{margin-bottom: 20px; margin-left: 3rem; margin-right: 3rem;}}
</style>
""", unsafe_allow_html=True)

skills = {
    "Programming & Databases": {
        "Languages": ["Python", "C++"],
        "Databases": ["MySQL", "PostgreSQL", "SQL Server"]
    },
    "Machine Learning, Data Science & Collection": {
        "Frameworks": ["Scikit-learn", "TensorFlow", "PyTorch"],
        "Data Processing": ["NumPy", "Pandas"],
        "Data Visualization": ["Matplotlib", "Seaborn"],
        "Natural Language Processing": ["NLTK", "spaCy"],
        "Web Scraping": ["Selenium", "BeautifulSoup", "Scrapy"]
    },
    "Web Development & DevOps": {
        "Web Frameworks": ["Django", "FastAPI"],
        "Containerization": ["Docker"],
        "Version Control": ["Git"],
        "Operating Systems": ["Linux"]
    },
    "Cloud & DevOps": {
        "Cloud Platforms": ["AWS"]
    }
}


st.markdown("<h1>My Technical Skills</h1>", unsafe_allow_html=True)

# Center the content
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    for category, subcategories in skills.items():
        st.markdown(f"<h2>{category}</h2>", unsafe_allow_html=True)
        for subcategory, items in subcategories.items():
            st.markdown(f"<h3>{subcategory}</h3>", unsafe_allow_html=True)
            st.markdown("<div class='subcategory'>" + 
                        "".join([f"<span class='skill-item'>{item}</span>" for item in items]) + 
                        "</div>", unsafe_allow_html=True)