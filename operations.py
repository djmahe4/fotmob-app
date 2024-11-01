import json
import matplotlib.pyplot as plt
import random
import seaborn as sns
import os
import requests
import numpy as np
import shutil
from datetime import date
import urllib.request
import urllib.parse

positions={2:"Midfielder",3:"Forward",1:"Defender",0:"Goalkeeper"}

def assesment(dict,vs):
    for x in dict:
        dict.update({x:performance(dict[x],vs)})
    return sorted(dict.items(),key=lambda x:x[1])
def performance(id,vs):
    response=requests.get(f"https://www.fotmob.com/api/playerData?id={id}")
    recent=json.loads(response.text)['recentMatches']
    #recent=response.json()['recentMatches']
    total=0
    matches=0
    for i in recent:
        if recent.index(i)<5:
            total += float(i['ratingProps']['num']) * 0.9
            matches += 1
        if i['opponentTeamName']==vs and float(i['ratingProps']['num'])!=0:
            total+=float(i['ratingProps']['num'])
            matches+=1
    try:
        return total/matches
    except ZeroDivisionError:
        return 0
def match_predict(match_id,st):
    params = {
        'matchId': f"{match_id}",
    }
    response = requests.get('https://www.fotmob.com/api/matchDetails', params=params)
    gem = response.json()
    # print(gem.keys())
    home = gem['general']['homeTeam']['name']
    away = gem['general']['awayTeam']['name']
    print(f"{home} vs {away}")
    st.write(f"**{home} vs {away}**")
    # print(gem['content'].keys())
    a = gem['content']
    # print(a["lineup"].keys())
    # print(len(a['lineup']['lineup']))
    hplayers = {}
    aplayers = {}
    # print(a['lineup2']['homeTeam']['starters'])
    # print(a['lineup2']['homeTeam']['subs'])
    # print(a['lineup2']['homeTeam']['unavailable'])
    try:
        for b in a['lineup']['homeTeam']['starters']:
            hplayers.update({b['name']: b["id"]})
    except TypeError or a['lineup']['homeTeam']['starters']==[]:
        st.write("lineup not available")
        return
    #if len(a['lineup']['homeTeam']['subs']) != 0:
        #for c in a['lineup']['homeTeam']['subs']:
            #hplayers.update({c['name']: c["id"]})
    for b in a['lineup']['awayTeam']['starters']:
        aplayers.update({b['name']: b["id"]})
    #if len(a['lineup']['awayTeam']['subs']) != 0:
        #for c in a['lineup']['homeTeam']['subs']:
            #aplayers.update({c['name']: c["id"]})

    hplayers = assesment(hplayers, away)
    aplayers = assesment(aplayers, home)
    print(hplayers)
    st.write(hplayers)
    print(aplayers)
    st.write(aplayers)

def match_id_init():
    #global st
    x = date.today()
    y = str(x).split('-')
    z = ''
    for i in y:
        z = z + i

    cookies = {
        'u:location': '%7B%22countryCode%22%3A%22IN%22%2C%22ccode3%22%3A%22IND%22%2C%22timezone%22%3A%22Asia%2FCalcutta%22%2C%22ip%22%3A%22111.92.78.166%22%2C%22regionId%22%3A%22KL%22%2C%22regionName%22%3A%22Kerala%22%7D',
        '_ga': 'GA1.1.948230614.1700192035',
        '_hjSessionUser_2585474': 'eyJpZCI6IjE5NTIyMWQ3LTVjNjctNTZhMS04M2RmLTlkNTYzYTdhNGE1MCIsImNyZWF0ZWQiOjE3MDAxOTIwMzQxNDAsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjIncludedInSessionSample_2585474': '0',
        '_hjSession_2585474': 'eyJpZCI6Ijg4MTZiODk1LWMwOTMtNDcwNS05MTg4LWQ0ZGFhM2U4OTg3YSIsImNyZWF0ZWQiOjE3MDAyMTgwMzI0MjQsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '__gads': 'ID=4a53b611dd8f2f33:T=1700192043:RT=1700218034:S=ALNI_MZ7af194OUe5cYcxUmjBR-_v_HLyw',
        '__gpi': 'UID=00000c8acce475e6:T=1700192043:RT=1700218034:S=ALNI_MZ-Y_BwyFNtH9dxlC_BaZ9_UJKBVg',
        '_ga_G0V1WDW9B2': 'GS1.1.1700217085.2.1.1700218036.56.0.0',
        'FCNEC': '%5B%5B%22AKsRol-61bjGXTm8QMYeD92wJtrXKIcUB3fkuYg_Iw5U2r4-k7roeKq36J3zIgpb8BlduaNRS_IByXzC69EVh7xVDn5zST0JvOgQ6kMhrNhySYQ9muHo6cFGDQAH90BJudlFaMD2f0wweyZXuUSzIbD6imGfcXlmKg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
        'g_state': '{"i_p":1700225255791,"i_l":1}',
    }

    headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.fotmob.com/?filter=time',
    'x-fm-req': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvbWF0Y2hlcz9kYXRlPTIwMjQxMDMxJnRpbWV6b25lPUFzaWElMkZDYWxjdXR0YSZjY29kZTM9SU5EIiwiY29kZSI6MTczMDM1MzMxMjA2Mn0sInNpZ25hdHVyZSI6IkQ2REVDNkNGQjFEMjhBOTE5NTVGNEIyRDk2N0UwNzRGIn0=',
    'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'sec-ch-ua-mobile': '?0',
    }
    response=requests.get('https://www.fotmob.com/api/mylocation')
    diction=json.loads(response.text)
    params = {
        'date': f'{z}',
        'timezone': diction['timezone'],#'Asia/Calcutta',
        'ccode3': diction['ccode3']#'IND',
    }
    #st.write(diction)
    print(diction)
    response = requests.get('https://www.fotmob.com/api/matches', params=params, headers=headers)
    #yes = response.json()
    yes=json.loads(response.text)

    a = yes["leagues"]
    b = []
    for i in a:
        # print(i.keys())
        c = [i['name'], i['matches']]
        leagueid = i['id']
        matches = []
        for x in i['matches']:
            score = []
            matchid = x['id']
            d = x['home']
            hname = d['longName']
            score.append(d['score'])
            e = x['away']
            aname = e['longName']
            score.append(e['score'])
            teams = [hname, aname]
            matches.append({matchid: [teams, score]})
        # b.append({"date":date.today()})
        b.append({leagueid: matches})
        with open("leagues.json", 'w') as file:
            # obj=json.load(open("leagues.json"))
            # obj["date"]=date.today()
            json.dump(b, file, indent=2)
    file.close()
    file=open("leagues.json","r",encoding="utf-8")
    contents=json.load(file)
    file.close()
    return contents

def analyze_player_stats(stats,st,name):
    analysis = f"**{name}:**\n"
    # x=stats["Player"].index(i)
    isgoalie = False

    # Positive aspects
    analysis += "\n+ves:\n"
    if 'expected_goals_on_target_faced' in stats and stats['expected_goals_on_target_faced'] < 0.5 and stats[
        'expected_goals_on_target_faced'] != 0:  # Adjust this threshold based on your criteria
        analysis += f"- Expected to face few on-target shots ({stats['expected_goals_on_target_faced']} xGOTF)\n"
        isgoalie = True

        if 'saves' in stats and stats['saves'] >= 5:
            analysis += f"- Had Saves: {stats['saves']}\n"
        if 'expected_goals_on_target_faced' in stats and stats[
            'expected_goals_on_target_faced'] > 0.3:  # Adjust this threshold based on your criteria
            analysis += f"- Expected to face on-target shots ({stats['expected_goals_on_target_faced']} xGOT)\n"
        if 'goals_prevented' in stats and stats['goals_prevented'] > 0:  # Adjust this threshold based on your criteria
            analysis += f"- Prevented {stats['goals_prevented']} goals\n"
        if 'accurate_passes' in stats and stats['accurate_passes'] > 20:
            analysis += f"- Had Good accurate passing ({stats['accurate_passes']} passes )\n"
        if 'recoveries' in stats and stats['recoveries'] >= 4:  # Adjust this threshold based on your criteria
            analysis += f"- Made {stats['recoveries']} recoveries\n"
        analysis += "\n-ves:\n"
        if 'minutes_played' in stats and stats['minutes_played'] <= 45:
            analysis += f"- Had Less game time ({stats['minutes_played']} minutes played)\n"
        if 'accurate_passes' in stats and stats['accurate_passes'] < 8:
            analysis += f"- Less accurate passes:({stats['accurate_passes']} )\n"
        if 'recoveries' in stats and stats['recoveries'] < 4:  # Adjust this threshold based on your criteria
            analysis += f"- Made insufficient ball recoveries ({stats['recoveries']} recoveries)\n"
        if 'goals_prevented' in stats and stats['goals_prevented'] < 0:  # Adjust this threshold based on your criteria
            analysis += f"- Prevented {stats['goals_prevented']} goals\n"
        if 'goals_conceded' in stats and stats['goals_conceded'] > 0:
            analysis += f"- Conceeded {stats['goals_conceded']} goals\n"
        analysis += "\nOverall Influence:\n"
        if ('rating_title' in stats and stats['rating_title'] > 7.0 and
                ('saves' in stats and stats['saves'] > 10 or
                 'goals_prevented' in stats and stats['goals_prevented'] > 2 or
                 'long_balls_accurate' in stats and stats['long_balls_accurate'] > 7 or
                 'touches_opp_box' in stats and stats['touches_opp_box'] > 5 or
                 'recoveries' in stats and stats['recoveries'] > 10)):
            # analysis += "- Significant overall influence on the game\n"

            analysis += "- Overall, a highly influential performance on the pitch\n\n"
        elif 'rating_title' in stats and stats['rating_title'] < 6.0:
            analysis += "- Needs improvement\n\n"
        else:
            analysis += "- A performance with both positive and negative aspects\n\n"
        st.write(analysis)
        return
    # if stats['rating_title'] > 7.0:
    # analysis += "- Impressive overall performance.\n"
    if 'chances_created' in stats and stats['chances_created'] > 0:
        analysis += f"- Created {stats['chances_created']} chances\n"
    if 'expected_goals' in stats and stats[
        'expected_goals'] > 0.5:  # Adjust this threshold based on your criteria
        analysis += f"- Expected to score goals ({stats['expected_goals']} xG)\n"
    if 'expected_goals_on_target_variant' in stats and stats[
        'expected_goals_on_target_variant'] > 0.5:  # Adjust this threshold based on your criteria
        analysis += f"- Expected to score goals on target ({stats['expected_goals']} xGOT)\n"
    if 'goals' in stats and stats['goals'] > 0:
        analysis += f"- {stats['goals']} goals\n"
    if 'assists' in stats and stats['assists'] > 0:
        analysis += f"- {stats['assists']} assists\n"
    if 'passes_into_final_third' in stats and stats['passes_into_final_third'] >= 6:  # Adjust this threshold based on your criteria
        analysis += f"- Successfully passed into the final third ({stats['passes_into_final_third']} times)\n"
    if 'xG Non-penalty' in stats and stats["xG Non-penalty"] > 0.2:  # Adjust this threshold based on your criteria
        analysis += f"- Was Dangerous infront of goal ({stats['xG Non-penalty']} xGNP)\n"
    if 'expected_assists' in stats and stats[
        'expected_assists'] > 0.2:  # Adjust this threshold based on your criteria
        analysis += f"- Expected to provide assists ({stats['expected_assists']} xA)\n"
    # ... add more positive aspects based on specific stats
    if 'accurate_crosses' in stats and stats['accurate_crosses'] > 3:  # Adjust this threshold based on your criteria
        analysis += f"- Successfully delivered accurate crosses ({stats['accurate_crosses']})\n"
    if 'duel_won' in stats and stats['duel_won'] >= 5:  # Adjust this threshold based on your criteria
        analysis += f"- Duels Won {stats['duel_won']}\n"
    if 'recoveries' in stats and stats['recoveries'] >= 4:  # Adjust this threshold based on your criteria
        analysis += f"- Made {stats['recoveries']} recoveries\n"
    if 'dribbles_succeeded' in stats and stats['dribbles_succeeded'] >= 5:  # Adjust this threshold based on your criteria
        analysis += f"- Successfully completed {stats['dribbles_succeeded']} of dribbles attempted\n"
    if 'was_fouled' in stats and stats['was_fouled'] >= 4:  # Adjust this threshold based on your criteria
        analysis += f"- Was fouled {stats['was_fouled']} times, drawing fouls\n"
    if 'blocked_shots' in stats and stats['blocked_shots'] > 0:  # Adjust this threshold based on your criteria
        analysis += f"- Blocked {stats['blocked_shots']} shots\n"
    if 'tackles_succeeded' in stats and stats['tackles_succeeded'] > 5:
        analysis += f"- Tackles successful : {stats['tackles_succeeded']}\n"
    if 'touches' in stats and stats['touches'] > 48:  # Adjust this threshold based on your criteria
        analysis += f"- Had {stats['touches']} touches, indicating active involvement in the game\n"
    if 'clearances' in stats and stats['clearances'] > 0:  # Adjust this threshold based on your criteria
        analysis += f"- Made {stats['clearances']} clearances\n"
    if 'accurate_passes' in stats and stats['accurate_passes'] > 20:
        analysis += f"- Had Good accurate passing ({stats['accurate_passes']} passes )\n"
    if 'defensive_actions' in stats and stats['defensive_actions'] > 0:  # Adjust this threshold based on your criteria
        analysis += f"- Had {stats['defensive_actions']} defensive action(s) during the game\n"
    if 'duel_lost' in stats and stats['duel_lost'] == 0:  # Adjust this threshold based on your criteria
        analysis += f"- Lost {stats['duel_lost']} duels\n"
    if 'ground_duels_won' in stats and stats['ground_duels_won'] > 5:  # Adjust this threshold based on your criteria
        analysis += f"- Won {stats['ground_duels_won']} ground duels\n"
    if 'shot_accuracy' in stats and stats['shot_accuracy'] > 0:
        analysis += f"- Accurate shots: {stats['shot_accuracy']}\n"
    if 'touches_opp_box' in stats and stats['touches_opp_box'] >= 5:  # Adjust this threshold based on your criteria
        analysis += f"- Had {stats['touches_opp_box']} touches in the opponent's box\n"
    if 'interceptions' in stats and stats['interceptions'] > 0:  # Adjust this threshold based on your criteria
        analysis += f"- Made {stats['interceptions']} interceptions\n"
    if 'aerials_won' in stats and stats['aerials_won'] > 5:  # Adjust this threshold based on your criteria
        analysis += f"- Aeriels won {stats['aerials_won']}\n"
    if 'long_balls_accurate' in stats and stats['long_balls_accurate'] > 6 and stats[
        'long_balls_accurate'] != 0:  # Adjust this threshold based on your criteria
        analysis += f"- Successful in playing accurate long balls ({stats['long_balls_accurate']} accuracy)\n"
    if 'long_balls_accurate'in stats and stats['long_balls_accurate'] < 4 and stats[
        'long_balls_accurate'] != 0:  # Adjust this threshold based on your criteria
        analysis += f"- Ineffective in playing accurate long balls: ({stats['long_balls_accurate']})\n"

    # Negative aspects
    analysis += "\n-ves:\n"
    if 'expected_goals_on_target_faced' in stats and stats['expected_goals_on_target_faced'] > 0.5 and stats[
        'expected_goals_on_target_faced'] != 0:  # Adjust this threshold based on your criteria
        analysis += f"- Expected to face high on-target shots ({stats['expected_goals_on_target_faced']} xGOTF)\n"
        isgoalie = True
    if 'rating_title' in stats and stats['rating_title'] < 6.0:
        analysis += "- Poor performance.\n"
    if 'minutes_played'in stats and stats['minutes_played'] <= 45:
        analysis += f"- Had Less game time ({stats['minutes_played']} minutes played)\n"
    if 'accurate_passes' in stats and stats['accurate_passes'] < 8:
        analysis += f"- Less accurate passes:({stats['accurate_passes']} )\n"
    # ... add more negative aspects based on specific stats
    if 'expected_goals' in stats and stats['expected_goals'] < 0.1 and stats[
        'expected_goals'] != 0:  # Adjust this threshold based on your criteria
        analysis += f"- Failed to generate significant goal-scoring opportunities ({stats['expected_goals']} xG)\n"
    if isgoalie==False and 'accurate_crosses' in stats and stats['accurate_crosses'] < 3 and stats[
        'accurate_crosses'] != 0:  # Adjust this threshold based on your criteria
        analysis += f"- Crosses were not accurate enough ({stats['accurate_crosses']})\n"
    if 'long_balls_accurate'in stats and stats['long_balls_accurate'] < 4 and stats[
        'long_balls_accurate'] != 0:  # Adjust this threshold based on your criteria
        analysis += f"- Ineffective in playing accurate long balls: ({stats['long_balls_accurate']})\n"
    if 'recoveries'in stats and stats['recoveries'] < 4:  # Adjust this threshold based on your criteria
        analysis += f"- Made insufficient ball recoveries ({stats['recoveries']} recoveries)\n"
    if 'dribbles_succeeded' in stats and stats['dribbles_succeeded'] < 3 and stats[
        'dribbles_succeeded'] != 0:  # Adjust this threshold based on your criteria
        analysis += f"- completed a low number of dribbles ({stats['dribbles_succeeded']})\n"
    if 'touches' in stats and stats['touches'] < 25:  # Adjust this threshold based on your criteria
        analysis += f"- Had {stats['touches']} touches, indicating less involvement in buildups\n"
    if 'dispossessed' in stats and stats['dispossessed'] > 0:  # Adjust this threshold based on your criteria
        analysis += f"- Was Dispossessed {stats['dispossessed']} times\n"
    if 'fouls' in stats and stats['fouls'] > 1:  # Adjust this threshold based on your criteria
        analysis += f"- Committed fouls {stats['fouls']} times\n"
    if isgoalie == False and 'defensive_actions' in stats and stats['defensive_actions'] == 0:  # Adjust this threshold based on your criteria
        analysis += f"- Was not active in any defensive action during the game\n"
    if 'duel_lost' in stats and stats['duel_lost'] > 4:  # Adjust this threshold based on your criteria
        analysis += f"- Lost {stats['duel_lost']} duels\n"
    if isgoalie == False and 'ground_duels_won' in stats and stats['ground_duels_won'] < 5 :  # Adjust this threshold based on your criteria
        analysis += f"- Won only {stats['ground_duels_won']} ground duels\n"
    if 'big_chance_missed_title' in stats and stats['big_chance_missed_title'] > 0:
        analysis += f"- Missed {stats['big_chance_missed_title']} big chances\n"
    if 'Offsides' in stats and stats['Offsides'] > 0:  # Adjust this threshold based on your criteria
        analysis += f"- Caught offside {stats['Offsides']} times\n"
    if 'dribbled_past' in stats and stats['dribbled_past'] > 0:  # Adjust this threshold based on your criteria
        analysis += f"- Was Dribbled past {stats['dribbled_past']} times\n"
    if 'aerials_won'in stats and stats['aerials_won'] < 5 and stats[
        'aerials_won'] != 0:  # Adjust this threshold based on your criteria
        analysis += f"- Aeriels won is only {stats['aerials_won']}\n"
    if 'saves' in stats and stats['saves'] < 5 and stats['saves']:
        analysis += f"- Saves: {stats['saves']}\n"


    # ... add more negative aspects based on specific stats

    # Overall Influence
    # Overall Influence
    analysis += "\nOverall Influence:\n"
    if ('rating_title' in stats and stats['rating_title'] > 7.0 and
            ('passes_into_final_third' in stats and stats['passes_into_final_third'] > 10 or
             'accurate_crosses' in stats and stats['accurate_crosses'] > 5 or
             ('duel_won' in stats and 'duel_lost' in stats and stats['duel_won'] >= 5 and stats['duel_lost'] < 5) or
             'dribbles_succeeded' in stats and stats['dribbles_succeeded'] >= 7 or
             'long_balls_accurate' in stats and stats['long_balls_accurate'] > 7 or
             'touches_opp_box' in stats and stats['touches_opp_box'] > 5 or
             'recoveries' in stats and stats['recoveries'] > 10)):
        #analysis += "- Significant overall influence on the game\n"

        analysis += "- Overall, a highly influential performance on the pitch\n\n"
    elif 'rating_title' in stats and stats['rating_title'] < 6.0:
        analysis += "- Needs improvement\n\n"
    else:
        analysis += "- A performance with both positive and negative aspects\n\n"
    st.write(analysis)

def headtohead(id,teams,score,st):
    file=open("impstats.json",'r')
    x=json.load(file)
    t1=[]
    t2=[]
    rem=[]
    keys=list(x.keys())
    #for i in keys:
        #ind=keys.index(i)
        #y=i.split('_')
        #if len(x)==1:
            #keys[ind]=i
            #continue
        #elif "expected" in y:
            #a=y[1:]
            #b=""
            #for i in a:
                #b=b+i[0].upper()
            #keys[ind]=f'x{b}'
    for i in x:
        if x[i][0]==x[i][1]==0 or x[i][0]==x[i][1]==None:
            rem.append(i)
            continue
        t1.append(x[i][0])
        t2.append(x[i][1])
    for i in rem:
        keys.remove(i)
    #print(t1)
    ls1={}
    ls2={}
    for i in t1:
        c = t1.index(i)
        if i==None:
            t1[c]=0
        #elif i==True or i==False:
            #t1.pop(t1.index(i))
        elif type(i)==str and "(" in i:
            a=i.split("(")
            b=a[1].split('%')
            #c=t1.index(i)
            t1[c]=float(a[0])
            t1[c]=round(t1[c], 2)
            ls1.update({keys[c]: f"{b[0]}%"})
        elif type(i)==str:
            a=float(i)
            b=t1.index(i)
            t1[b]=round(a, 2)
    for i in t2:
        c = t2.index(i)
        if i == None:
            t2[c] = 0
        # elif i==True or i==False:
        # t1.pop(t1.index(i))
        elif type(i) == str and "(" in i:
            a = i.split("(")
            b = a[1].split('%')
            #c = t2.index(i)
            t2[c] = float(a[0])
            t2[c] = round(t2[c], 2)
            ls2.update({keys[c]: f"{b[0]}%"})
        elif type(i) == str:
            a = float(i)
            b = t2.index(i)
            t2[b] = round(a, 2)
    print(keys)
    val1=t1.copy()
    val2=t2.copy()
    val2 = [-abs(x) for x in val2]
    t2 = [-abs(x) for x in t2]
    #print(t1)
    #print(t2)

    # Create a figure and a set of subplots with increased size
    fig, ax = plt.subplots(figsize=(15, 15))  # Adjust as needed
    plt.style.use('ggplot')  # Use the 'ggplot' style
    # Set the y positions
    y_pos = np.arange(len(keys))

    # Create a color palette
    colors=sns.color_palette("bright")
    # Randomly select two distinct colors
    color1, color2 = random.sample(colors, 2)
    # Create the horizontal bars with the new colors
    bar1 = ax.barh(y_pos, t1, color=color1, label=f'{teams[0]}')
    bar2 = ax.barh(y_pos, t2, color=color2, label=f'{teams[1]}')

    # ... your existing code ...
    # Set the y-axis limits to make smaller bars appear larger
    #ax.set_xlim([-max(max(t1), max(t2)) * 1.2, max(max(t1), max(t2)) * 1.2])

    # Add the category names as y-tick labels with increased font size
    ax.set_yticks(y_pos)
    ax.set_yticklabels(keys, fontsize=12)  # Adjust as needed
    # Add gridlines
    ax.grid(True, linestyle='--', alpha=0.6)

    # Sort bars
    t1, t2, keys = zip(*sorted(zip(t1, t2, keys)))

        # Hide the y-axis values
    ax.yaxis.set_tick_params(length=0)

        # Add the stat values beside the bars
    for i, v in enumerate(val1):
        ax.text(v + 1, i, str(v), color='black', va='center')
    for i, v in enumerate(val2):
        ax.text(v - 1, i, str(abs(v)), color='black', va='center', ha='right')

        # Add watermark with Twitter handle
    plt.text(0.5, 0.5, '@DJMahe04', fontsize=14, ha='center', va='center', alpha=0.5, transform=ax.transAxes)
    # Create a string with the keys and values from 'ls'
    ls_text = "\n".join(f"{k}: {v}" for k, v in ls1.items())

    # Add the text box to the plot
    ax.text(0.8, -0.05, ls_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor=color1, alpha=0.5))
    # Create a string with the keys and values from 'ls'
    ls_text = "\n".join(f"{k}: {v}" for k, v in ls2.items())

    # Add the text box to the plot
    ax.text(0.1, -0.05, ls_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor=color2, alpha=0.5))
    ax.legend(loc='upper right')
    plt.title(f'[{score[1]}] {teams[1]} vs {teams[0]} [{score[0]}]', size=16, weight='bold', color='#333333')
    #plt.savefig(f'{id}/team_comparison.jpg', dpi=100, bbox_inches='tight')
    st.pyplot(fig)
    file.close()
def subdataext(id,record,records):
    global positions
    l=[]
    x=record
    #print(x)
    #print(x.keys())
    try:
        position=positions[id['usualPlayingPositionId']]
    except KeyError:
        print("line178")
        print(id)
    name=id['name']
    #fname=name['fullName']
    stats=x[str(id['id'])]["stats"]
    #print("stats",stats)
    stats0=stats[:]
    #print(stats0)
    rstats={}
    l = []
    for i in range(len(stats0)):
        stats00 = stats0[i]
        only = stats00['stats']
        print("only", only)
        for key in only:
            try:
                l.append({only[key]['key']:only[key]['stat']['value']})
                fraction_str = f"{only[key]['stat']['value']}/{only[key]['stat']['total']}"

                # Split the string into numerator and denominator
                #numerator, denominator = map(int, fraction_str.split('/'))

                # Calculate the percentage
                #try:
                    #percentage = (numerator / denominator) * 100
                #except ZeroDivisionError:
                    #percentage=0
                l.append({f"{only[key]['key']}%": fraction_str})
            except KeyError:
                continue
    l.append({"position": position})
    records.update({name: l})
    return records
def match_details(id):
    global anew
    mainstats = {}
    records={}
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
    # 'cookie': '__gpi=UID=00000de55eeafc9b:T=1712677321:RT=1712677321:S=ALNI_Mbzxe_PMDTNBzcRWRn2EjB3ptaQAA; _ga=GA1.1.2076984740.1712677318; _cc_id=7be34bda8ef5c90644fbb00c411b806b; g_state={"i_p":1729939157741,"i_l":3}; u:location=%7B%22countryCode%22%3A%22IN%22%2C%22ccode3%22%3A%22IND%22%2C%22timezone%22%3A%22Asia%2FCalcutta%22%2C%22ip%22%3A%222406%3A8800%3A9015%3A1570%3A396e%3Aec8b%3Ab96e%3A7a7f%22%2C%22regionId%22%3A%22KL%22%2C%22regionName%22%3A%22Kerala%22%7D; panoramaId_expiry=1730956138989; panoramaId=a7e77b7fe87c1cd7d758189a0e4416d539384ed4a4570b7f8b2da0a1f43435c9; panoramaIdType=panoIndiv; cto_bundle=NyJUGV9XdHpnQ0lrS0x2VUdmcU93UGZNUWd2RXpTRzVzVjM5V3JBbkRWYmQyOTVtZTFyejJXJTJGS0dKZjBoUDRYc1phakI5UWJYaE0xdVhRN1Fzdjhvc3Y3WjJPa3RKZ3ZZTiUyRlRRMzh5ekVRM2lORVV4Q1QlMkZMRVlvVGJia01Iak1aa3VYdTAwcGpBVklURHdQTXZqaHppYjR6emclM0QlM0Q; FCNEC=%5B%5B%22AKsRol9qpaNl4wm4MHOVezEtDiaTFBAh353e5-QjRWlllse4_D_907sNl4siF5a2ML9LC0BCsULBHscW6NdB9Oj3Q-lQaFmNL4_4kj-D24LRG9R0I-N0lL0M4ilmKgp11LNCbAqcSimus1GuGQcIS4nFQCG0hg0QUw%3D%3D%22%5D%5D; __gads=ID=faa1e9087fd1c078:T=1712677321:RT=1730353286:S=ALNI_Ma6L5CmpnceQeaPqEFWmPNRuYfEgA; __eoi=ID=66fbdc7ff144ff21:T=1729334344:RT=1730353286:S=AA-Afjb4iGP-5-EUcCydc8gEb6xn; _ga_G0V1WDW9B2=GS1.1.1730351331.8.1.1730353576.0.0.0',
    'priority': 'u=1, i',
    'referer': 'https://www.fotmob.com/matches/beasain-vs-cartagena/26wpcm',
    'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    'x-fm-req': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvbWF0Y2hEZXRhaWxzP21hdGNoSWQ9NDY1NjQzMyIsImNvZGUiOjE3MzAzNTM1Nzg3Nzd9LCJzaWduYXR1cmUiOiJFRjEwQ0RCMTRGMjBCMTVGMDYxRTAxNjQ3MDYzRTc2NSJ9',
}
    params = {
        'matchId': f'{id}',
    }
    directory_path = f'{id}'
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    response = requests.get('https://www.fotmob.com/api/matchDetails', params=params, headers=headers)
    gem = response.json()
    # for i in gem:
    # print(i)
    #print(gem)
    a = gem["content"]
    anew=gem
    b = a['playerStats']
    lin = a['lineup']
    sub = lin['homeTeam']['subs']
    for i in sub:
        try:
            if i["performance"]['substitutionEvents'][0]['time']  < 90:
                subdataext(i, b,records)
        except KeyError as e:
            #print(i["performance"]['substitutionEvents'][0]['time'])
            print(e)
            print("line 230")
            #print(i,records)
            #exit(0)
            continue
    sub = lin['awayTeam']['subs']
    for i in sub:
        try:
            if i["performance"]['substitutionEvents'][0]['time']  < 90:
                subdataext(i, b,records)
        except KeyError:
            continue
    e1 = gem['header']
    extrac = e1["teams"]
    tm1 = extrac[0]['name']
    tm2 = extrac[1]['name']
    score = [extrac[0]['score'], extrac[1]['score']]
    print(score)
    # extrac=extrac["lineup"][0]
    # print(extrac.keys())
    teamnames = [tm1, tm2]
    #headtohead(id, teamnames, score)
    # extrac=extrac["lineup"][1]
    # teamnames.append(extrac["teamName"])
    print(teamnames)
    b = a['stats']
    c = b['Periods']
    d = c['All']
    e = d["stats"]
    f = e[0]
    # substitute(f)
    g = f['stats']
    for i in range(len(e)):
        f = e[i]
        g = f['stats']
        mainstats.update({f['key']: f['stats']})
    stz = {}
    with open("impstats.json", 'w') as file:
        ax = list(mainstats.keys())
        for i in range(len(mainstats)):
            j = mainstats[ax[i]]
            # print(j)
            k = j[0]
            for i in j:
                k = i["key"]
                l = i["stats"]
                print(k, l)
                x = stz.update({k: l})
        json.dump(stz, file)
    return a,teamnames,score,records
def get_player_stats(a,records):
    global anew
    b = a["lineup"]
    try:
        c = b['homeTeam']['starters']
    except KeyError:
        print(b.keys())
    # x = c.pop()
    y = b['awayTeam']['starters']
    a = anew["content"]
    b = a['playerStats']
    for i in c:
        subdataext(i, b,records)
    # print()
    # exit(0)
    # print(y)
    # lineup=y['lineup'][0]
    # ben1=lineup['bench']
    for i in y:
        subdataext(i, b,records)
    return records
def plotting(records,st):
    new_rec={}
    colors = sns.color_palette("husl", 12)
    for i in records:
        name = i
        pos = records[i][-1]['position']
        dic = records[i]
        # dic.pop("fantasy_points")
        #try:
            #rating = dic["rating_title"]
        #except KeyError:
            #rating = None
        x = dic.copy()
        #st.write(name)
        #st.write(pos)
        #st.write(dic)
        #x.update({"rating": rating})

        # Process dictionary values
        ls = {}
        for key in enumerate(dic):
            #st.write(key[0])
            keys = list(dic[key[0]].keys())[0]
            val = list(dic[key[0]].values())[0]
            #st.write(keys)
            #st.write(val)
            if val is None:
                x.remove(dic[key[0]])
            elif isinstance(val, bool):
                x.remove(dic[key[0]])
            elif isinstance(val, str) and "/" in val:
                #a = val.split("(")
                #b = a[1].split("%")
                #x[key[0]] = float(b[0])
                x.remove(dic[key[0]])
                ls.update({keys: val})
            elif isinstance(val, str) and "%" in keys:
                #a = val.split("/")
                #b = a[1].split("%")
                #x[key[0]] = float(b[0])
                x.remove(dic[key[0]])
                ls.update({keys: val})
            elif isinstance(val, str):
                try:
                    x[key[0]] = float(val)
                except ValueError:
                    x.remove(dic[key[0]])
        #st.write("newtest")
        #st.write(ls)
        #return
        #x.pop()
        print(x)
        haha=x.copy()
        #y = list(x.keys())
        #z = list(x.values())
        y = []
        z = []
        for dictionary in x:
            y.extend(dictionary.keys())
            z.extend(dictionary.values())
        new_rec[name] = y
        # Normalize data to fit within the range [0, 1]
        real = z.copy()
        zc = z.copy()
        for value in z:
            ind = zc.index(value)
            try:
                if float(value) is None or value <= 0.1:
                    zc.pop(ind)
                    y.pop(ind)
                    real.pop(ind)
                elif int(value) < 1:
                    zc[ind] = value * 100
                elif int(value) < 10:
                    zc[ind] = value * 10
            except TypeError as e:
                print(e)


        color1, color2, color3 = random.sample(colors, 3)
        max_stat = max(zc)
        normalized_stats = [(stat - 0) / (max_stat - 0) for stat in zc]

        # Number of categories
        for i in y:
            ind = y.index(i)
            if i == 'rating_title':
                y[ind] = 'rating'
        num_categories = len(y)

        # Step 2: Calculate the angle for each category
        angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()
        # Step 3: Close the plot
        normalized_stats += [normalized_stats[0]]
        angles += [angles[0]]
        # Step 4: Create the plot
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        # ax.set_ylim(0, 0.8)

        # Plot the data
        ax.plot(angles, normalized_stats, 'o-', linewidth=2, color=color1, markersize=8, alpha=0.7)
        ax.fill(angles, normalized_stats, color=color1, alpha=0.3)

        # ax.set_aspect("equal")
        ax.margins(len(y) / 30)

        # Set category labels on the plot with clear font
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(y, fontsize=6, weight='bold', color=color2, rotation_mode="anchor")

        # Textbox
        for i, (angle, stat, label) in enumerate(zip(angles, real, y)):
            x = angle + np.pi / 2 if angle < np.pi else angle - np.pi / 2
            y = normalized_stats[i] + 0.355
            text = f"{int(stat)}" if isinstance(stat, int) else f"{float(stat)}"
            ax.text(angle, y, text, fontsize=8, ha='center', va='center', color=color3,
                    bbox=dict(boxstyle='square', facecolor='white'))

        # Add watermark with Twitter handle
        plt.text(-0.05, -0.05, '@DJMahe04', fontsize=12, ha='center', va='center', alpha=0.2, transform=ax.transAxes)

        # Create a string with the keys and values from 'ls'
        ls_text = "\n".join(f"{k}: {v}" for k, v in ls.items())

        # Add the text box to the plot
        ax.text(1.2, 0.25, ls_text, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.4))

        # Step 6: Display the plot
        plt.title(f'Player Performance {name} ({pos})', size=16, weight='bold', color='#333333')
        st.pyplot(fig)
        combined_dict = {}
        for d in haha:
            combined_dict.update(d)
        analyze_player_stats(combined_dict,st,name)
        #return
#a,teamnames,score,records=match_details("4621519") #here records includes the stats of subs in dictionary with stats as key list
#get_player_stats(a)
#print("records",records) #now records are complete
