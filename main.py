import os
os.popen("pip install -r requirements.txt")
import streamlit as st
import requests
import json
from operations import headtohead,match_details,get_player_stats,plotting,match_id_init,match_predict
#from operations import *
from num_fotmob import main as numerology

# Streamlit UI
st.title("Fotmob Analyser")
contents=match_id_init()
#file=open("leagues.json","r",encoding="utf-8")
#contents=json.load(file)
#file.close()
choices={}
for x in contents:
    for y in x.values():
        #print(y)
        #choices.append(y)
        for z in y:
            record=list(z.values())[0]
            match=f'{record[0][0]} vs {record[0][1]}: {record[1][0]}-{record[1][1]}'
            choices.update({match:list(z.keys())[0]})
#print(choices)
choice=st.selectbox("Match",list(choices.keys()))
print(choice)
print()
match_id=choices[choice]
st.write(f"Selected match: {choice}")
st.write(f"Match ID: {match_id}")
types_of_analysis=["head to head","playerwise","future prediction","numerology"]
choice=st.selectbox("Analysis Type",types_of_analysis)
st.write(f"Selected analysis type: {choice}")
print(choice)
if choice=="head to head":
    a,teamnames,score,records=match_details(match_id)
    headtohead(match_id,teamnames,score,st)
elif choice=="playerwise":
    a,teamnames,score,records=match_details(match_id)
    #headtohead(match_id,teamnames,score,st)
    get_player_stats(a,records)
    print("records", records)
    plotting(records,st)
elif choice=="future prediction":
    match_predict(match_id,st)
elif choice=="numerology":
    numerology(match_id,st)
