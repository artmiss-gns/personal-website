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

        # <h4>Academic Achievements:</h4>
        # <ul>
        #     <li>Consistently maintained a position in the top 10% of the class throughout the program</li>
        #     <li>Received highest grades in Machine Learning and Artificial Intelligence courses</li>
        #     <li>Selected as a Teaching Assistant for Algorithms and Data Structures (Fall 2023)</li>
        # </ul>

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


show()