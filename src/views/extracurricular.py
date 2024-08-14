from streamlit import session_state as ss

if 'sidebar_state' not in ss:
    ss.sidebar_state = 'expanded'
else :
    if ss.sidebar_state != 'expanded':
        ss.sidebar_state = 'expanded'