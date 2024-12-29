import requests
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import seaborn as sns
import time

def get_season_stats_destruct():
    st.session_state.pposition=None
    st.session_state.per90=False
def get_season_stats(name,id=1083323,season="LaLiga"):
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
    # 'cookie': '__gpi=UID=00000de55eeafc9b:T=1712677321:RT=1712677321:S=ALNI_Mbzxe_PMDTNBzcRWRn2EjB3ptaQAA; _ga=GA1.1.2076984740.1712677318; _cc_id=7be34bda8ef5c90644fbb00c411b806b; _ga_G0V1WDW9B2=deleted; _hjSessionUser_2585474=eyJpZCI6IjIxZDk5Y2IyLWYzYWItNWU4My04MjZkLTg4ZWQzNTJiNjhiZCIsImNyZWF0ZWQiOjE3MzI0NTQ1NDEwOTgsImV4aXN0aW5nIjp0cnVlfQ==; g_state={"i_p":1737618382846,"i_l":4}; panoramaId_expiry=1736003449444; panoramaId=5c722abb08b9f1805376473591f916d539387d1ff0076b4717d6c24ad5065d37; panoramaIdType=panoIndiv; u:location=%7B%22countryCode%22%3A%22IN%22%2C%22ccode3%22%3A%22IND%22%2C%22timezone%22%3A%22Asia%2FCalcutta%22%2C%22ip%22%3A%222406%3A8800%3A9015%3Ac550%3Abc05%3Aad0d%3A5d4b%3A4802%22%2C%22regionId%22%3A%22KL%22%2C%22regionName%22%3A%22Kerala%22%7D; _hjSession_2585474=eyJpZCI6IjE2NjJhMTNjLTIzM2ItNGI1ZC04NmMxLWVmODYxOTgxMmNlYyIsImMiOjE3MzU0NDI2MTI4ODAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; cto_bundle=1DwFRV9XdHpnQ0lrS0x2VUdmcU93UGZNUWdzTHJmN0JrWGJ2SHRLWHo1cndhWiUyQnU1WjZDJTJCVERkMUlIVDVJWURvUGdTMFQlMkJMbXRjQU54ZXBmZGw2QXlKWWlMUnpydmxUNGl6Y2FnZXdjOGgwaTd2Mm1oQmp5YUZWSjkyTzZpMHZUZEV5Q1NwWU9reUMlMkI0QnNEWkZyREpSVW5nQSUzRCUzRA; FCNEC=%5B%5B%22AKsRol8dfE0ocUW_ZVrdxyczwL6vMQnD0yA-5vbJtpQuCHQvOfD7D4ZK2DdRu-1MAS8ksKRHRqlLIzVzJHTo5t5Ix6in_jYagItNoz0BmkVWjJFOTbRiGKyFPAiekYHAkY-O82HKbQ56O3YdmB3a6oTRCQXQKtVucw%3D%3D%22%5D%5D; _ga_G0V1WDW9B2=GS1.1.1735442611.17.1.1735444281.0.0.0; __gads=ID=faa1e9087fd1c078:T=1712677321:RT=1735444291:S=ALNI_Ma6L5CmpnceQeaPqEFWmPNRuYfEgA; __eoi=ID=66fbdc7ff144ff21:T=1729334344:RT=1735444291:S=AA-Afjb4iGP-5-EUcCydc8gEb6xn',
    'priority': 'u=1, i',
    'referer': f'https://www.fotmob.com/players/{id}/{"-".join(name.lower().split())}',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'x-mas': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvcGxheWVyRGF0YT9pZD0xNjk3MTgiLCJjb2RlIjoxNzM1NDQ0Mjg4MDA1LCJmb28iOiJlOTZiNjBhMjEifSwic2lnbmF0dXJlIjoiNUI4QjQzQTdDRjQ5NDFGQjJDNDk4NzlBMzMxNzU4N0QifQ==',
}

    params = {
        'id': f'{id}',
    }
    try:
        response = requests.get('https://www.fotmob.com/api/playerData', params=params, headers=headers)
        response.json()
    except requests.JSONDecodeError:
        st.write("Waiting")
        time.sleep(5)
        get_season_stats(name,id,season)
    for i in response.json()['statSeasons'][0]['tournaments']:
        if i['name']==season:
            print(i["entryId"])
            eid=i["entryId"]
    #eid="0-1"
    st.write(eid)
    if eid!="0-0":
        headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.fotmob.com/players/1083323/pedri',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'x-mas': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvcGxheWVyU3RhdHM/cGxheWVySWQ9MTA4MzMyMyZzZWFzb25JZD0wLTEmaXNGaXJzdFNlYXNvbj1mYWxzZSIsImNvZGUiOjE3MzU0NDg2MjI1NDIsImZvbyI6ImU5NmI2MGEyMSJ9LCJzaWduYXR1cmUiOiIzM0FENzdFNzI5NTk2OTVBRDFGRERFM0JEQjMxQkFFOCJ9',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
}

        params = {
            'playerId': f'{id}',
            'seasonId': f'{eid}',
            #'isFirstSeason': 'false',
        }

        response = requests.get('https://www.fotmob.com/api/playerStats', params=params, headers=headers)
        b=response.json()['statsSection']['items']
    else:
        b=response.json()['firstSeasonStats']['statsSection']['items']
    #print(b)
    if "pposition" not in st.session_state:
        st.session_state.pposition=None
    if "per90" not in st.session_state:
        st.session_state.per90=False
    desired = {
        "Goalkeeper": [
            "Saves",
            "Save percentage",
            "Goals conceded"
            "Goals prevented",
            "Clean sheets",
            "High claim",
            "Pass accuracy",
            "Long ball accuracy"
        ],
        "Centre-Back": [
            "Tackles won",
            "Duels won",
            "Aerial duels won",
            "Interceptions",
            "Blocked",
            "Recoveries",
            'Dribbled past',
            "Successful passes",
            "Pass accuracy",
            "Accurate long balls",
            "Touches"
        ],
        "Full-Back/Wing-Back": [
            "xA",
            "Duels won",
            "Interceptions",
            "Blocked",
            "Recoveries",
            "Successful dribbles",
            "Successful passes",
            "Pass accuracy",
            "Accurate long balls",
            "Touches",
            "Successful crosses",
            "Cross accuracy"
        ],
        "Defensive Midfielder": [
            "Assists",
            "Interceptions",
            "Successful passes",
            "Pass accuracy",
            "Tackles won",
            "Duels won",
            "Accurate long balls",
            "Touches",
            "Dispossessed",
            "Tackles won",
            "Interceptions",
            "Recoveries",
            'Dribbled past'
        ],
        "Central Midfielder": [
            "Assists",
            "xA",
            "Successful passes",
            "Pass accuracy",
            "Accurate long balls",
            "Chances created",
            "Successful dribbles",
            "Touches",
            "Dispossessed",
            "Tackles won",
            "Interceptions",
            "Recoveries",
            "Possession won final 3rd"
        ],
        "Wide Midfielder/Winger": [
            "Goals",
            "xG",
            "Shots",
            "Shots on target",
            "Assists",
            "xA",
            "Successful dribbles",
            "Touches in opposition box",
            "Successful crosses",
            "Cross accuracy",
            "Interceptions"
        ],
        "Forward/Striker": [
            "Goals",
            "xG",
            "Shots",
            "Shots on target",
            "Assists",
            "xA",
            "Successful dribbles",
            "Touches in opposition box",
            "Duels won",
            "Recoveries"
        ]
    }
    if st.session_state.pposition:  # Only display if a position has been selected
        st.write(f"Selected position: {st.session_state.pposition}")
    pos=st.selectbox("Choose position to analyse:",list(desired.keys()))
    if pos != st.session_state.pposition: #check if the choice has changed
        st.session_state.pposition = None
        st.session_state.per90 = False
        #st.session_state.choice2 = pos
    if st.button("Position selected"):
        st.session_state.pposition=pos
    present=[]
    necessary = []
    for i in b[:-1]:
        print(i['title'])
        for items in i["items"]:
            present.append(items["title"])
            if items["title"] in desired[st.session_state.pposition]:
                necessary.append(items)
                print(items["title"])
    print(necessary)
    print(present)
    #p9 = input("Per 90 stats (y/n):")
    if st.session_state.per90:  # Only display if a position has been selected
        st.write(f"Per 90: {st.session_state.per90}")
    p9=st.selectbox("Per90?",[True,False])
    if pos != st.session_state.per90: #check if the choice has changed
        #st.session_state.pposition = None
        st.session_state.per90 = None
        #st.session_state.choice2 = pos
    if st.button("Done.."):
        st.session_state.per90=p9
    # Convert the data into a pandas DataFrame
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(necessary)
    # Convert 'statValue' to numeric
    df['statValue'] = pd.to_numeric(df['statValue'])
    df['per90'] = pd.to_numeric(df['per90'])
    df['percentileRankPer90'] = pd.to_numeric(df['percentileRankPer90'])
    df['percentileRank'] = pd.to_numeric(df['percentileRank'])
    # Assuming 'df' is your DataFrame
    df.drop(columns=['localizedTitleId', 'statFormat'], inplace=True)
    rdf = df
    print(rdf)
    st.dataframe(rdf)
    # Create a color palette
    palette = sns.color_palette("bright", len(df))
    # Create the bar plot
    plt.figure(figsize=(20, 10))
    if st.session_state.per90:
        bar_plot = sns.barplot(x='title', y='percentileRankPer90', data=df, palette=palette)
        # Display the 'per90' above the bars
        for i, row in df.iterrows():
            bar_plot.text(i, row.percentileRankPer90 + 0.5, round(row.per90, 2), color='black', ha="center")
    else:
        bar_plot = sns.barplot(x='title', y='percentileRank', data=df, palette=palette)
        # Display the 'statValue' above the bars
        for i, row in df.iterrows():
            bar_plot.text(i, row.percentileRank + 0.5, round(row.statValue, 2), color='black', ha="center")

    plt.axhline(50, color='red', linestyle='dashed')

    # Rotate x-axis labels for better visibility
    # plt.xticks(rotation=90, fontsize=10)

    # Set plot title and labels
    #name = input("Enter player name:")
    # tname=input("Enter season:")
    plt.title(f'Season Stats of {name.title()} in {season}', fontsize=20, color=random.choice(palette))
    plt.xlabel('Stats', fontsize=15, color='green')
    plt.ylabel('Percentile ranking', fontsize=15, color='red')

    # Adjust the subplot parameters to give the x-axis labels more space
    plt.subplots_adjust(bottom=0.4)
    st.pyplot(plt)
    #return
def season_comparison_destruct():
    st.session_state.atype1 = None
    st.session_state.atype2 = None
def season_comparison(id):
    if "atype1" not in st.session_state:
        st.session_state.atype1=None
    if "atype2" not in st.session_state:
        st.session_state.atype2=None
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
        # 'cookie': '__gpi=UID=00000de55eeafc9b:T=1712677321:RT=1712677321:S=ALNI_Mbzxe_PMDTNBzcRWRn2EjB3ptaQAA; _ga=GA1.1.2076984740.1712677318; _cc_id=7be34bda8ef5c90644fbb00c411b806b; _ga_G0V1WDW9B2=deleted; _hjSessionUser_2585474=eyJpZCI6IjIxZDk5Y2IyLWYzYWItNWU4My04MjZkLTg4ZWQzNTJiNjhiZCIsImNyZWF0ZWQiOjE3MzI0NTQ1NDEwOTgsImV4aXN0aW5nIjp0cnVlfQ==; panoramaId_expiry=1735383329968; panoramaId=804c193543df94bdaf3775cce9894945a702c8a27ba6aba96dc7c0055b26d49c; panoramaIdType=panoIndiv; g_state={"i_p":1737618382846,"i_l":4}; u:location=%7B%22countryCode%22%3A%22IN%22%2C%22ccode3%22%3A%22IND%22%2C%22timezone%22%3A%22Asia%2FCalcutta%22%2C%22ip%22%3A%222406%3A8800%3A9015%3Ac550%3A656f%3Ae4c5%3A6e5d%3Afccd%22%2C%22regionId%22%3A%22KL%22%2C%22regionName%22%3A%22Kerala%22%7D; FCNEC=%5B%5B%22AKsRol8JTFw79ztvqk-5Oj_ln5gMDeR-dbmk8vkQL_pSpwrxMFGSJVIONhQ24JMi7_y3sIWohteiYErlSoBiP_SNI84QAb-CHeTUSR6HlD12jIfkx98d_AOklODngKjut0UWdUVOXycSDwNy5CFXKXpeC45VripyUw%3D%3D%22%5D%5D; cto_bundle=hI4bU19XdHpnQ0lrS0x2VUdmcU93UGZNUWdyU0tWUmVuOE9LbHRZWU1LU1ZlQkhwUWxTUmIxZE82U1VTbGdQb0Rkbk9VbUNuYTFldDhiTDZDZlJrNHVzJTJGNW1udXZYbVEyaW1PRVVsWjh2VnhjYlolMkYlMkZ0Q0hNJTJCc2JKRjlQUGE5Qkx3N0R5VnV0SUdua1B2Zmp4MXJINDVtUDVYdyUzRCUzRA; _hjSession_2585474=eyJpZCI6ImJhYjVjZDczLTdkZjQtNDVlMy04NjA4LWE3N2M1NzcwNjdlYyIsImMiOjE3MzUzMTMzMTA4MTAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _ga_G0V1WDW9B2=GS1.1.1735313308.13.1.1735313314.0.0.0; __gads=ID=faa1e9087fd1c078:T=1712677321:RT=1735313335:S=ALNI_Ma6L5CmpnceQeaPqEFWmPNRuYfEgA; __eoi=ID=66fbdc7ff144ff21:T=1729334344:RT=1735313335:S=AA-Afjb4iGP-5-EUcCydc8gEb6xn',
        'if-none-match': '"zstzs34g1ublce"',
        'priority': 'u=1, i',
        'referer': 'https://www.fotmob.com/leagues/42/overview/champions-league',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'x-mas': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvbGVhZ3Vlcz9pZD00MiZjY29kZTM9SU5EJm5ld1VlZmFCcmFja2V0PXRydWUiLCJjb2RlIjoxNzM1MzEzMzcwNTU1LCJmb28iOiJlOTZiNjBhMjEifSwic2lnbmF0dXJlIjoiQjI5ODQ3M0M1MURCQTE2RTdCOUY5RTY2RkQ4M0VFRkQifQ==',
    }

    params = {
        'id': f'{id}',
        'ccode3': f'{st.session_state.ccode3}',
    }

    response = requests.get('https://www.fotmob.com/api/leagues', params=params, headers=headers)
    #print(response)
    a = response.json()
    #print(a)
    stats = a["stats"]["players"]
    di = {}
    for i in stats:
        di.update({i["header"]: i["fetchAllUrl"]})
    # print(di)

    comp = {
        "Goals per 90": "Assists",
        "Expected goals (xG)": "Goals per 90",
        "Big chances created": "Assists",
        "Successful dribbles per 90": "Goals + Assists",
        "Clean sheets": "Save percentage",
        "Interceptions per 90": "Possession won final 3rd per 90",
        "Expected goals (xG) per 90": "Goals per 90",
        "Shots on target per 90": "Goals per 90",
        "Shots per 90": "Expected goals (xG)",
        "Accurate passes per 90": "Assists",
        "Big chances missed": "Goals per 90",
        "Penalties won": "Goals per 90",
        # "Successful tackles per 90": "Interceptions per 90",
        "Clearances per 90": "Blocks per 90",
        "Goals conceded per 90": "Clean sheets",
        "Fouls committed per 90": "Red cards",
        # "Expected goals (xG)": "Assists",
        "Accurate long balls per 90": "Assists",
        "Expected assist (xA)": "Assists",
        "xG + xA per 90": "Goals + Assists",
        # "Successful dribbles per 90": "Chances created",
        "Successful tackles per 90": "Blocks per 90",
        "Save percentage": "Goals prevented",
        # "Fouls committed per 90": "Yellow cards",
        "Possession won final 3rd per 90": "Goals per 90"
    }
    comments = [
        "Analyzes the relationship between scoring and assisting.",
        "Compares expected goals with actual goals scored.",
        "Understands how creating chances translates to assists.",
        "Analyzes the impact of dribbling on direct goal contributions.",
        "Evaluates the goalkeeper's performance.",
        "Assesses defensive effectiveness in the final third.",
        "Evaluates the efficiency of a player in scoring compared to the expected rate.",
        "Sees how shots on target correlate with actual goals scored.",
        "Analyzes the quality of shots taken.",
        "Determines the impact of passing accuracy on creating goal opportunities.",
        "Understands the impact of missed opportunities on a player's goal tally.",
        "Assesses the contribution of penalties won to the total number of goals.",
        # "Compares defensive actions and their frequency.",
        "Evaluates different aspects of defensive play.",
        "Observes the relationship between the frequency of conceding goals and keeping clean sheets.",
        "Explores the severity of fouls and their consequences.",
        # "Explores the relationship between xG and assists.",
        "Analyzes the impact of accurate long balls on assists.",
        "Assesses the contribution of xA to assists.",
        "Evaluates the efficiency of xG and xA combined.",
        # "Analyzes the impact of successful dribbles on creating chances.",
        "Assesses defensive contributions to preventing goals.",
        "Evaluates the goalkeeper's impact on preventing goals.",
        # "Explores disciplinary actions related to fouls.",
        "Explores the impact of winning possession in the final third on scoring."
    ]
    keyvals=[x+" vs "+comp[x] for x in comp]
    if st.session_state.atype1 is None:
        atype=st.radio("Select analysis type",keyvals,captions=comments)
        if st.button("Analysis selected!"):
            st.session_state.atype1=atype.split(" vs ")[0]
            st.session_state.atype2 = atype.split(" vs ")[1]
            stat1=st.session_state.atype1
            stat2=st.session_state.atype2
            # Get the data
            data1 = requests.get(di[stat1]).json()["TopLists"][0]["StatList"]
            data2 = requests.get(di[stat2]).json()["TopLists"][0]["StatList"]

            # Assume the data is a list of dictionaries with 'player' and 'value' keys
            # players1 = [d['ParticipantName'] for d in data1]
            # players2 = [d['ParticipantName'] for d in data2]
            data1_dict = {d['ParticipantName']: d['StatValue'] for d in data1}
            data2_dict = {d['ParticipantName']: d['StatValue'] for d in data2}
            # Get all players
            # all_players = set(list(data1_dict.keys()) + list(data2_dict.keys()))

            # Prepare the data for scatter plot
            players = []
            # stat1_values = []
            # stat2_values = []
            # Get the intersection of the two sets of players
            common_players = list(set(list(data1_dict.keys())) & set(list(data2_dict.keys())))

            # Filter the data to include only the common players
            stat1_values = [data1_dict[player] for player in common_players]
            stat2_values = [data2_dict[player] for player in common_players]

            # Create a DataFrame from the data
            df = pd.DataFrame({
                'Player': common_players,
                stat1: stat1_values,
                stat2: stat2_values
            })
            # Sort the DataFrame by stat1 and get the top 5 players
            top5_stat1 = df.sort_values(by=stat1, ascending=False).head(5)

            # Sort the DataFrame by stat2 and get the top 5 players
            top5_stat2 = df.sort_values(by=stat2, ascending=False).head(5)

            # Concatenate the two dataframes
            top5_both = pd.concat([top5_stat1, top5_stat2])

            # Remove duplicates
            top5_both = top5_both.drop_duplicates()

            # Reset index
            top5_both = top5_both.reset_index(drop=True)
            print(top5_both)
            st.dataframe(top5_both)
            #tname = input("Enter league name:")
            # feedback = f"This a dataframe: {top5_both} ;it contains season wise comparison of {stat1} vs {stat2}. Make a twitter thread analysing both the stats (of current season), both critical and optimistic and human type."

            palette = sns.color_palette("bright", 3)
            color1, color2, color3 = random.sample(palette, 3)
            # Create the scatterplot with seaborn
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df, x=stat1, y=stat2, palette='hls')  # hls
            sns.set_style("whitegrid")
            plt.title(f'{list(st.session_state.returned.keys())[0]} {stat1} vs {stat2}', fontsize=14, color=color1)
            plt.xlabel(stat1, fontsize=12, color=color2)
            plt.ylabel(stat2, fontsize=12, color=color3)
            for i, player in enumerate(common_players):
                plt.annotate(player, (stat1_values[i], stat2_values[i]))
            # Avoid overlapping
            plt.tight_layout()
            st.pyplot(plt)
