import streamlit as st

def show():
    st.title("Education")

    # Custom CSS for better styling
    st.markdown("""
        <style>
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
            <li>Special Topics in Computer Science (Machine Learning/Deep Learning): A+ (19/20)</li>
            <li>Artificial Intelligence: A+ (18.5/20)</li>
            <li>Data Structures and Algorithms: A (17.8/20)</li>
            <li>Nonlinear Optimization: A (17.8/20)</li>
            <li>Linear Optimization: A (17/20)</li>
            <li>Algorithm Design: A (16.1/20)</li>
        </ul>
        <h4>Academic Achievements:</h4>
        <ul>
            <li>Consistently maintained a position in the top 10% of the class throughout the program</li>
            <li>Received highest grades in Machine Learning and Artificial Intelligence courses</li>
            <li>Selected as a Teaching Assistant for Algorithms and Data Structures (Fall 2023)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Additional Academic Experiences
    st.header("Additional Academic Experiences")

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

    # Future Education Plans
    st.header("Future Education Plans")

    st.markdown("""
    <div class="education-item">
        <h3>Graduate Studies Aspirations</h3>
        <ul>
            <li>Actively pursuing opportunities for graduate studies in Computer Science with a focus on Machine Learning and Artificial Intelligence</li>
            <li>Interested in programs that offer strong research components in Natural Language Processing and Information Retrieval</li>
            <li>Aiming to contribute to cutting-edge research and push the boundaries of AI technology</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Continuous Learning
    st.header("Continuous Learning")

    st.markdown("""
    <div class="education-item">
        <h3>Online Courses and Certifications</h3>
        <ul>
            <li>Completed the Deep Learning Specialization by Andrew Ng on Coursera</li>
            <li>Actively participating in Kaggle competitions to apply and enhance machine learning skills</li>
            <li>Regular attendee of local and online AI and Machine Learning meetups and workshops</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Call the show function to display the page content
show()