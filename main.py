import os
os.popen("pip install -r requirements.txt")
import streamlit as st
import requests
import json
from operations import headtohead, match_details, get_player_stats, plotting, match_id_init, match_predict
from num_fotmob import main as numerology

# Streamlit UI
st.title("Fotmob Analyser")

# Define a button to start the analysis after choices are made
if 'match_selected' not in st.session_state:
    st.session_state.match_selected = False

if st.button("Start Analysis"):
    contents = match_id_init()  # Only calls match_id_init once
    choices = {}
    for x in contents:
        for y in x.values():
            for z in y:
                record = list(z.values())[0]
                match = f'{record[0][0]} vs {record[0][1]}: {record[1][0]}-{record[1][1]}'
                choices.update({match: list(z.keys())[0]})

    st.session_state.choices = choices
    st.session_state.match_selected = True

# Show dropdowns only after the "Start Analysis" button is clicked
if st.session_state.match_selected:
    choice = st.selectbox("Match", list(st.session_state.choices.keys()))
    match_id = st.session_state.choices[choice]
    st.write(f"Selected match: {choice}")
    st.write(f"Match ID: {match_id}")

    types_of_analysis = ["head to head", "playerwise", "future prediction", "numerology"]
    analysis_choice = st.selectbox("Analysis Type", types_of_analysis)
    st.write(f"Selected analysis type: {analysis_choice}")

    # Trigger analysis based on the selected type
    match analysis_choice:
        case "head to head":
            a, teamnames, score, records = match_details(match_id)
            headtohead(match_id, teamnames, score, st)
        case "playerwise":
            a, teamnames, score, records = match_details(match_id)
            headtohead(match_id, teamnames, score, st)
            get_player_stats(a, records)
            plotting(records, st)
        case "future prediction":
            match_predict(match_id, st)
        case "numerology":
            numerology(match_id, st)
