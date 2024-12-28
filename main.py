import os
# os.popen("pip install -r requirements.txt")
import streamlit as st
import requests
from operations import headtohead, match_details, get_player_stats, plotting, match_id_init, match_predict
from num_fotmob import main as numerology
from datetime import datetime
from individual_analysis import main as indiv

# Streamlit UI
st.title("Fotmob Analyser")
st.write(datetime.today())

# Toggle for individual stats analysis
on = st.toggle("Keep it on to analyze individual stats..")
if on==True:
    st.session_state.switch = True
    det = requests.get("https://www.fotmob.com/api/mylocation").json()
    st.write(det)
    st.session_state.ccode3 = det["ccode3"]
    indiv()  # Call the individual analysis function

# Initialize session state variables if not already done or if toggle is off
if 'match_selected' not in st.session_state or not on:
    st.session_state.choice2 = None
    st.session_state.mmid = None
    st.session_state.toa = None
    st.session_state.match_selected = False
    st.session_state.timezone = False
    st.session_state.ccode3 = False
    st.session_state.country = None
    st.session_state.switch = False
    st.session_state.pname = None
    st.session_state.confirmed = False
    st.session_state.choices=None

# Button to start the analysis after choices are made (only if toggle is off)
if st.button("Start") and not st.session_state.switch:
    det = requests.get("https://www.fotmob.com/api/mylocation").json()
    st.session_state.timezone = det['timezone']
    st.session_state.ccode3 = det['ccode3']
    
    # Fetch match details and populate choices
    contents = match_id_init()  # Only calls match_id_init once
    choices = {}
    for x in contents:
        for y in x.values():
            for z in y:
                record = list(z.values())[0]
                match = f'{record[0][0]} vs {record[0][1]}: {record[1][0]}-{record[1][1]}'
                choices[match] = list(z.keys())[0]

    st.session_state.choices = choices
    #st.session_state.match_selected = True

# Show dropdowns only after the "Start Analysis" button is clicked and matches are selected
if st.session_state.choices and not st.session_state.mmid:
    choice = st.selectbox("Match", list(st.session_state.choices.keys()))
    match_id = st.session_state.choices[choice]
    st.write(f"Selected match: {choice}")
    st.write(f"Match ID: {match_id}")
    if st.button("match selected"):
        st.session_state.match_selected = True
    # Store selected match ID in session state
        st.session_state.mmid = match_id
if st.session_state.mmid:
    types_of_analysis = ["head to head", "playerwise", "future prediction", "numerology"]
    analysis_choice = st.selectbox("Analysis Type", types_of_analysis)
    
    if st.button("Start analysis") and st.session_state.match_selected:
        st.write(f"Selected analysis type: {analysis_choice}")
        st.session_state.toa = analysis_choice

        # Trigger analysis based on the selected type
        if st.session_state.toa == "head to head":
            a, teamnames, score, records = match_details(st.session_state.mmid)
            headtohead(st.session_state.mmid, teamnames, score)
        elif st.session_state.toa == "playerwise":
            a, teamnames, score, records = match_details(st.session_state.mmid)
            headtohead(match_id, teamnames, score)
            get_player_stats(a, records)
            plotting(records)
        elif st.session_state.toa == "future prediction":
            match_predict(st.session_state.mmid)
        elif st.session_state.toa == "numerology":
            numerology(st.session_state.mmid, st)
