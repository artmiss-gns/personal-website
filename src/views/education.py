import streamlit as st
from streamlit import session_state as ss

if 'sidebar_state' not in ss:
    ss.sidebar_state = 'expanded'
    # ss.sidebar_state = "collapsed"
else :
    if ss.sidebar_state != 'expanded':
        ss.sidebar_state = 'expanded'
    # if ss.sidebar_state != 'collapsed':
        # ss.sidebar_state = 'collapsed'

primaryColor = "#279095"
backgroundColor = "#eff3f9"
secondaryBackgroundColor = "#D1D6DC"
textColor = "#333333"
font = "sans serif"

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
        font-size: 40px;
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

st.markdown("""
    <style>
    .main > div {
        padding-top: 3rem;
    }
    .education-item {
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 2rem;
    }
    .education-item h3 {
        margin-top: 0;
    }
    .highlight {
        font-weight: bold;
        color: #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Education")


# University of Isfahan
st.markdown("""
<div class="education-item">
    <h3>University of Isfahan</h3>
    <p><span class="highlight">Bachelor of Science (BS) in Computer Science</span><br>
    2020 - 2024 (Expected Graduation)</p>
    <ul>
        <li>Overall GPA: 3.18/4.0</li>
        <li>Last 2 years GPA (62 credits): 3.47/4.0</li>
        <li>Ranked in the top 10% of class</li>
    </ul>
    <h4>Selected Coursework:</h4>
    <ul>
        <li><b>Special Topics in Computer Science (Machine Learning/Deep Learning)</b>: <span style="color: #3e8e41;">A+ (19/20)</span></li>
        <li><b>Artificial Intelligence</b>: <span style="color: #3e8e41;">A+ (18.5/20)</span></li>
        <li><b>Data Structures and Algorithms</b>: <span style="color: #3e8e41;">A (17.8/20)</span></li>
        <li><b>Nonlinear Optimization</b>: <span style="color: #3e8e41;">A (17.8/20)</span></li>
        <li><b>Linear Optimization</b>: <span style="color: #3e8e41;">A (17/20)</span></li>
        <li><b>Algorithm Design</b>: <span style="color: #3e8e41;">A (16.1/20)</span></li>
        <li><b>Computer Networks</b>: <span style="color: #3e8e41;">A (16.5/20)</span></li>
        <li><b>Numeric Linear Algebra</b>: <span style="color: #3e8e41;">A (16/20)</span></li>
        <li><b>Compiler Design</b>: <span style="color: #3e8e41;">A (17/20)</span></li>
        <li><b>Database Design</b>: <span style="color: #3e8e41;">A (16/20)</span></li>
    </ul>

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="education-item">
    <h3>Teaching Assistant Experience</h3>
    <p><span class="highlight">Algorithms and Data Structures</span> - Fall 2023</p>
    <ul>
        <li>Developed course materials and designed challenging coding problems</li>
        <li>Graded exams and assignments, providing constructive feedback</li>
        <li>Collaborated with faculty to enhance course content and student learning outcomes</li>
        <li>Demonstrated strong organizational, communication, and problem-solving skills</li>
    </ul>
</div>
""", unsafe_allow_html=True)
