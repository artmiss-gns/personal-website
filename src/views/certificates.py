import streamlit as st
import PyPDF2
import base64
from pathlib import Path

primaryColor = "#279095"
backgroundColor = "#eff3f9"
secondaryBackgroundColor = "#D1D6DC"
textColor = "#333333"
font = "sans serif"

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
        font-size: 30px;
        margin-bottom: 20px;
        text-align: center;
        border-bottom: 2px solid {primaryColor};
        padding-bottom: 10px;

    }}
    h2 {{
        color: {primaryColor};
        font-size: 20px;

    }}
    h3 {{
        color: {textColor};
        font-size: 30px;
    }}
""", unsafe_allow_html=True)



def display_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    return pdf_display

def display_certificate(pdf_path, cert_id, course_name, institution, completion_date):
    col1, col2 = st.columns([3, 4])
    
    with col1:
        st.subheader(course_name)
        st.write(f"**Issued by:** {institution}")
        st.write(f"**Completed on:** {completion_date}")
        st.write(f"**Certificate ID:** {cert_id}")
        
        # Validation button
        coursera_url = f"https://www.coursera.org/account/accomplishments/certificate/{cert_id}"
        st.markdown(f"[Verify Certificate on Coursera]({coursera_url})")

    with col2:
        st.markdown(display_pdf(pdf_path), unsafe_allow_html=True)

    st.divider()  # Add a divider between certificates

st.title("My Coursera Certificates")

# List of your certificates with local file paths and details
certificates = [
    {
        "id": "N4NY92BV4N3K",
        "path": "src/static/certificates_pdf/Coursera N4NY92BV4N3K.pdf",
        "course": "Unsupervised Learning, Recommenders, Reinforcement Learning",
        "institution": "Stanford University",
        "date": "October 12, 2023"
    },
    {
        "id": "RYVXZ4A3VBZW",
        "path": "src/static/certificates_pdf/Coursera RYVXZ4A3VBZW.pdf",
        "course": "Supervised Machine Learning: Regression and Classification",
        "institution": "Stanford University",
        "date": "July 31, 2023"
    },
    {
        "id": "Q4SKG3KBKGR7",
        "path": "src/static/certificates_pdf/Coursera Q4SKG3KBKGR7.pdf",
        "course": "Advanced Learning Algorithms",
        "institution": "Stanford University",
        "date": "August 27, 2023"
    },
]

for cert in certificates:
    display_certificate(
        cert["path"],
        cert["id"],
        cert["course"],
        cert["institution"],
        cert["date"]
    )