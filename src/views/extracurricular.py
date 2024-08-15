import streamlit as st
from streamlit import session_state as ss
from streamlit_carousel import carousel

if 'sidebar_state' not in ss:
    # ss.sidebar_state = 'expanded'
    ss.sidebar_state = "collapsed"
else :
    # if ss.sidebar_state != 'expanded':
    #     ss.sidebar_state = 'expanded'
    if ss.sidebar_state != 'collapsed':
        ss.sidebar_state = 'collapsed'

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

st.markdown("""
    <style>
    .main > div {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)


st.title("Extracurricular")

project_cards = [
    {
        "title": "",
        "img": "src/static/images/PsyCity/PsyCity1.png",
        "text": "",
    },
    {
        "title": "",
        "img": "src/static/images/PsyCity/PsyCity2.png",
        "text": "",
    },
    {
        "title": "",
        "img": "src/static/images/PsyCity/PsyCity3.png",
        "text": "",
    },
    {
        "title": "",
        "img": "src/static/images/PsyCity/PsyCity4.png",
        "text": "",
    },
]


c1, c2 = st.columns([3, 2])
with c1:
    st.header("Psycity Nationwide Coding Contest")
    
    st.markdown("""
    As the Algorithm Section Head for the 'Psycity' Nationwide Coding Contest, I played a crucial role in shaping this significant programming event. My responsibilities included:

    - **Leading Algorithmic Problem Design**: Over a six-month preparation period, I spearheaded the creation of challenging and engaging algorithmic questions. This task required deep technical knowledge and creativity to ensure a high-quality competition.

    - **Team Management**: I led a team of problem setters, coordinating their efforts to develop a cohesive and balanced set of questions for the contest.

    - **Contest Oversight**: During the three-day event, I actively managed both on-site and online participation for approximately 100 contestants. This dual-format approach required careful planning and execution to ensure fairness and smooth operations for all participants.

    - **Crisis Management**: We faced a critical server issue during the contest, which tested our problem-solving skills under pressure. My team and I successfully resolved the problem, minimizing disruption to the event.

    - **Technical Support**: Throughout the contest, I provided technical assistance, addressing issues promptly to maintain the integrity of the competition.

    This experience significantly enhanced my skills in leadership, crisis management, and teamwork. It also deepened my understanding of large-scale event organization in the tech sphere. The success of 'Psycity' demonstrated our ability to create and manage a complex, nationwide coding contest, setting a high standard for future events.
    """)


with c2:
    carousel(items=project_cards, container_height=400)