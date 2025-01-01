import os
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
if on:
    st.session_state.switch = True
    det = requests.get("https://www.fotmob.com/api/mylocation").json()
    st.write(det)
    st.session_state.ccode3 = det["ccode3"]
    st.session_state.country=det["countryCode"]
    st.session_state.returned = {}
    #st.session_state.returned2 = {}
    st.session_state.opt4 = None
    st.session_state.keyvals=[]
    st.session_state.seasonsu=False
    indiv()

# Initialize session state variables (more comprehensive)
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
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
    st.session_state.choices = {}

# Button to start the analysis (only if individual stats toggle is off)
if st.button("Start") and not st.session_state.switch:
    det = requests.get("https://www.fotmob.com/api/mylocation").json()
    st.session_state.timezone = det['timezone']
    st.session_state.ccode3 = det['ccode3']

    contents = match_id_init(st)
    choices = {}
    for x in contents:
        for y in x.values():
            for z in y:
                record = list(z.values())[0]
                match = f'{record[0][0]} vs {record[0][1]}: {record[1][0]}-{record[1][1]}'
                choices[match] = list(z.keys())[0]

    st.session_state.choices = choices
    #Reset match selection states when Start is pressed
    st.session_state.match_selected = False
    st.session_state.mmid = None
    st.session_state.toa = None

# Match Selection Section (Now with reset logic)
if st.session_state.choices:
    if st.session_state.match_selected: # Only display this if a match has been selected
        st.write(f"Selected match: {st.session_state.selected_match_display}")
        st.write(f"Match ID: {st.session_state.mmid}")
    else:
        choice = st.selectbox("Match", list(st.session_state.choices.keys()))
        if choice != st.session_state.choice2:#check if the choice has changed
            st.session_state.match_selected = False
            st.session_state.mmid = None
            st.session_state.toa = None
            st.session_state.choice2 = choice
            #st.experimental_rerun() #force rerun so the selectbox updates correctly
            st.rerun()
        if st.button("Match selected"):
            st.session_state.match_selected = True
            st.session_state.mmid = st.session_state.choices[choice]
            st.session_state.selected_match_display = choice # Store display string

# Analysis Type Selection (Conditional Display)
if st.session_state.match_selected:
    if st.session_state.toa is None:
        types_of_analysis = ["head to head", "playerwise", "future prediction", "numerology"]
        analysis_choice = st.selectbox("Analysis Type", types_of_analysis)
        if st.button("Start analysis"):
            st.write(f"Selected analysis type: {analysis_choice}")
            st.session_state.toa = analysis_choice

# Trigger Analysis
if st.session_state.toa and st.session_state.switch==False:
    if st.session_state.toa == "head to head":
        a, teamnames, score, records = match_details(st.session_state.mmid,st)
        headtohead(st.session_state.mmid, teamnames, score,st)
    elif st.session_state.toa == "playerwise":
        a, teamnames, score, records = match_details(st.session_state.mmid,st)
        headtohead(st.session_state.mmid, teamnames, score)
        get_player_stats(a, records,st)
        plotting(records,st)
    elif st.session_state.toa == "future prediction":
        match_predict(st.session_state.mmid)
    elif st.session_state.toa == "numerology":
        numerology(st.session_state.mmid, st)
