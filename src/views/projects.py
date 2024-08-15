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

def main():
    github_logo = "src/static/logos/github-logo.png"


    logo_container = st.container()
    logo_container.image(github_logo, width=150)

    # Add some margin to the bottom of the logo
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Custom CSS for a cool, minimalist look
    st.markdown("""
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .big-font {
        font-size: 60px !important;
        font-weight: bold;
        margin-bottom: 20px;

    }
    .medium-font {
        font-size: 24px !important;
        margin-bottom: 40px;
    }
    .github-link {
        font-size: 24px;
        text-decoration: none;
        padding: 15px 30px;
        background-color: #1b6a6f;
        border-radius: 30px;
        transition: all 0.3s;
        color: white !important;
    }

    .github-link:hover {
        text-decoration: none; /* Ensure underline is removed on hover */
        color: white !important; /* Force text color to remain white on hover */
        background-color: #0D5458; /* Darker shade of green on hover */
        transform: scale(1.05);
    }


    </style>
    """, unsafe_allow_html=True)

    # Content
    st.markdown("""
    <div class="container">
        <p class="big-font">Welcome to My Coding Universe</p>
        <p class="medium-font">Explore my projects and contributions</p>
        <a href="https://github.com/artmiss-gns" target="_blank" class="github-link">Visit My GitHub</a>
    </div>
    """, unsafe_allow_html=True)


main()
