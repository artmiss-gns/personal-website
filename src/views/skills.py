import streamlit as st

def show():
    st.title("Skills")

    # Custom CSS for better styling
    st.markdown("""
        <style>
        .skill-category {
            background-color: #2c3c44;
            border-radius: 10px;
            padding: 1.5rem;
            margin-bottom: 2rem;
        }
        .skill-category h3 {
            margin-top: 0;
            color: #eac61a;
        }
        .skill-item {
            background-color: #e2f1e9;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            margin: 0.5rem 0;
            display: inline-block;
            margin-right: 0.5rem;
            color: #2c3c44;
        }
        .proficiency-bar {
            height: 10px;
            background-color: #d3d3d3;
            border-radius: 5px;
            margin-top: 5px;
        }
        .proficiency-level {
            height: 100%;
            background-color: #4CAF50;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Programming Languages
    st.markdown("""
    <div class="skill-category">
        <h3>Programming Languages</h3>
        <div class="skill-item">Python <div class="proficiency-bar"><div class="proficiency-level" style="width: 95%;"></div></div></div>
        <div class="skill-item">C++ <div class="proficiency-bar"><div class="proficiency-level" style="width: 80%;"></div></div></div>
        <div class="skill-item">SQL <div class="proficiency-bar"><div class="proficiency-level" style="width: 85%;"></div></div></div>
        <div class="skill-item">Java <div class="proficiency-bar"><div class="proficiency-level" style="width: 70%;"></div></div></div>
    </div>
    """, unsafe_allow_html=True)

    # Machine Learning & Data Science
    st.markdown("""
    <div class="skill-category">
        <h3>Machine Learning & Data Science</h3>
        <div class="skill-item">Scikit-learn <div class="proficiency-bar"><div class="proficiency-level" style="width: 90%;"></div></div></div>
        <div class="skill-item">TensorFlow <div class="proficiency-bar"><div class="proficiency-level" style="width: 85%;"></div></div></div>
        <div class="skill-item">PyTorch <div class="proficiency-bar"><div class="proficiency-level" style="width: 80%;"></div></div></div>
        <div class="skill-item">NumPy <div class="proficiency-bar"><div class="proficiency-level" style="width: 95%;"></div></div></div>
        <div class="skill-item">Pandas <div class="proficiency-bar"><div class="proficiency-level" style="width: 90%;"></div></div></div>
        <div class="skill-item">NLTK <div class="proficiency-bar"><div class="proficiency-level" style="width: 75%;"></div></div></div>
    </div>
    """, unsafe_allow_html=True)

    # Web Development
    st.markdown("""
    <div class="skill-category">
        <h3>Web Development</h3>
        <div class="skill-item">FastAPI <div class="proficiency-bar"><div class="proficiency-level" style="width: 85%;"></div></div></div>
        <div class="skill-item">Django <div class="proficiency-bar"><div class="proficiency-level" style="width: 80%;"></div></div></div>
        <div class="skill-item">Streamlit <div class="proficiency-bar"><div class="proficiency-level" style="width: 90%;"></div></div></div>
        <div class="skill-item">HTML/CSS <div class="proficiency-bar"><div class="proficiency-level" style="width: 75%;"></div></div></div>
    </div>
    """, unsafe_allow_html=True)

    # Cloud & Deployment
    st.markdown("""
    <div class="skill-category">
        <h3>Cloud & Deployment</h3>
        <div class="skill-item">AWS <div class="proficiency-bar"><div class="proficiency-level" style="width: 70%;"></div></div></div>
        <div class="skill-item">Docker <div class="proficiency-bar"><div class="proficiency-level" style="width: 80%;"></div></div></div>
        <div class="skill-item">Git <div class="proficiency-bar"><div class="proficiency-level" style="width: 90%;"></div></div></div>
    </div>
    """, unsafe_allow_html=True)

    # Databases
    st.markdown("""
    <div class="skill-category">
        <h3>Databases</h3>
        <div class="skill-item">MySQL <div class="proficiency-bar"><div class="proficiency-level" style="width: 85%;"></div></div></div>
        <div class="skill-item">PostgreSQL <div class="proficiency-bar"><div class="proficiency-level" style="width: 80%;"></div></div></div>
        <div class="skill-item">SQL Server <div class="proficiency-bar"><div class="proficiency-level" style="width: 75%;"></div></div></div>
    </div>
    """, unsafe_allow_html=True)

    # Soft Skills
    st.markdown("""
    <div class="skill-category">
        <h3>Soft Skills</h3>
        <div class="skill-item">Problem Solving</div>
        <div class="skill-item">Team Collaboration</div>
        <div class="skill-item">Project Management</div>
        <div class="skill-item">Technical Writing</div>
        <div class="skill-item">Public Speaking</div>
    </div>
    """, unsafe_allow_html=True)

    # Additional Information
    st.header("Continuous Learning")
    st.write("""
    I am constantly expanding my skill set and staying up-to-date with the latest technologies. 
    Some areas I'm currently focusing on include:
    - Advanced Natural Language Processing techniques
    - Graph Neural Networks
    - MLOps and model deployment at scale
    - Quantum Computing basics
    """)

    st.header("Certifications")
    st.write("""
    - Deep Learning Specialization (Coursera)
    - Machine Learning (Stanford Online)
    - AWS Certified Cloud Practitioner
    """)

# Call the show function to display the page content
show()