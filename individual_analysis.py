import streamlit as st
import requests,json
from check import get_season_stats,season_comparison,get_season_stats_destruct,season_comparison_destruct

positions={2:"Midfielder",3:"Forward",1:"Defender",0:"Goalkeeper"}
def psearch(name):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
        # 'cookie': '__gpi=UID=00000de55eeafc9b:T=1712677321:RT=1712677321:S=ALNI_Mbzxe_PMDTNBzcRWRn2EjB3ptaQAA; _ga=GA1.1.2076984740.1712677318; _cc_id=7be34bda8ef5c90644fbb00c411b806b; _ga_G0V1WDW9B2=deleted; _hjSessionUser_2585474=eyJpZCI6IjIxZDk5Y2IyLWYzYWItNWU4My04MjZkLTg4ZWQzNTJiNjhiZCIsImNyZWF0ZWQiOjE3MzI0NTQ1NDEwOTgsImV4aXN0aW5nIjp0cnVlfQ==; panoramaId_expiry=1735383329968; panoramaId=804c193543df94bdaf3775cce9894945a702c8a27ba6aba96dc7c0055b26d49c; panoramaIdType=panoIndiv; cto_bundle=6VXOlF9XdHpnQ0lrS0x2VUdmcU93UGZNUWdyWFhzJTJCNkNndXAlMkJXWndpOHI0SEF5NFFpOExtMlZoWUglMkJ6VW1MMzJGMGd3WHhraWpNajNyTm1yRDhpZnBKRDVnaXBsSnl0anF0MWx6QXBiZHZvQ1NXMmhxd1g4YndzelpJNjVoblBZWHlRYXUlMkZHNVI4NXFqbk9FdmxuREFNMFVVdyUzRCUzRA; g_state={"i_p":1737618382846,"i_l":4}; u:location=%7B%22countryCode%22%3A%22IN%22%2C%22ccode3%22%3A%22IND%22%2C%22timezone%22%3A%22Asia%2FCalcutta%22%2C%22ip%22%3A%222406%3A8800%3A9015%3Ac550%3Aeca6%3A44f2%3Affeb%3A2379%22%2C%22regionId%22%3A%22KL%22%2C%22regionName%22%3A%22Kerala%22%7D; _hjSession_2585474=eyJpZCI6Ijk4ZjUzOTBhLTY2ODgtNDQxMy04NWNkLTljNzg5YjliN2NkNCIsImMiOjE3MzUyMDU5NTEzMTgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __gads=ID=faa1e9087fd1c078:T=1712677321:RT=1735205957:S=ALNI_Ma6L5CmpnceQeaPqEFWmPNRuYfEgA; __eoi=ID=66fbdc7ff144ff21:T=1729334344:RT=1735205957:S=AA-Afjb4iGP-5-EUcCydc8gEb6xn; FCNEC=%5B%5B%22AKsRol-7wz6Zzh_kziamYUpXqMUFBf9S_ja9qzOGSERxIX9L1XjEQCLwLC0WC5UpJSl1b3ZTYhjLKV5oiqD-FX-vQ4T_6MQoUt3YtyQ5uWRAl5VwMfuFRJ4Fig4pxLFaFrCIQ30ql5GzT73cpm10ULrSlcHjpEZy_g%3D%3D%22%5D%5D; _ga_G0V1WDW9B2=GS1.1.1735205896.6.1.1735206031.0.0.0',
        'if-none-match': '"10gql3603y2al"',
        'priority': 'u=1, i',
        'referer': 'https://www.fotmob.com/',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'x-mas': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvc2VhcmNoL3N1Z2dlc3Q/aGl0cz01MCZsYW5nPWVuJnRlcm09YWRyaWFuK2x1bmEiLCJjb2RlIjoxNzM1MjA2MDU2NDM2LCJmb28iOiJlOTZiNjBhMjEifSwic2lnbmF0dXJlIjoiMURFNENGNDQ2RDVFOEExMjM3RDI2MEYxRUFDQ0NGQzUifQ==',
    }

    params = {
        'hits': '50',
        'lang': 'en',
        'term': f'{name}',
    }

    response = requests.get('https://www.fotmob.com/api/search/suggest', params=params,
                            headers=headers)
    st.write(response.status_code)
    return response.json()[0]['suggestions']['id'],response.json()[0]['suggestions']['id']
def squad_extract(id):
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://www.fotmob.com/teams/1642068/squad/auckland-fc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'x-mas': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvdGVhbXM/aWQ9MTY0MjA2OCZjY29kZTM9SU5EIiwiY29kZSI6MTczNTI3MDI5MzM3MywiZm9vIjoiZTk2YjYwYTIxIn0sInNpZ25hdHVyZSI6IjVFMzk4QTVGMkU0Q0Q4OUIwRUNCOTU2MDc0RjE2NkI3In0=',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
    }

    params = {
        'id': f'{id}',
        'ccode3': f'{st.session_state.country}',
    }

    response = requests.get('https://www.fotmob.com/api/teams', params=params, headers=headers)
    #print(response.json())
    det=response.json()
    players = {}
    for i in det['squad'][1:]:
        for j in i['members']:
            players.update({j['name']: j['id']})
    return players
def season_team_extract(id):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
        # 'cookie': '__gpi=UID=00000de55eeafc9b:T=1712677321:RT=1712677321:S=ALNI_Mbzxe_PMDTNBzcRWRn2EjB3ptaQAA; _ga=GA1.1.2076984740.1712677318; _cc_id=7be34bda8ef5c90644fbb00c411b806b; _ga_G0V1WDW9B2=deleted; _hjSessionUser_2585474=eyJpZCI6IjIxZDk5Y2IyLWYzYWItNWU4My04MjZkLTg4ZWQzNTJiNjhiZCIsImNyZWF0ZWQiOjE3MzI0NTQ1NDEwOTgsImV4aXN0aW5nIjp0cnVlfQ==; panoramaId_expiry=1735383329968; panoramaId=804c193543df94bdaf3775cce9894945a702c8a27ba6aba96dc7c0055b26d49c; panoramaIdType=panoIndiv; cto_bundle=6VXOlF9XdHpnQ0lrS0x2VUdmcU93UGZNUWdyWFhzJTJCNkNndXAlMkJXWndpOHI0SEF5NFFpOExtMlZoWUglMkJ6VW1MMzJGMGd3WHhraWpNajNyTm1yRDhpZnBKRDVnaXBsSnl0anF0MWx6QXBiZHZvQ1NXMmhxd1g4YndzelpJNjVoblBZWHlRYXUlMkZHNVI4NXFqbk9FdmxuREFNMFVVdyUzRCUzRA; g_state={"i_p":1737618382846,"i_l":4}; u:location=%7B%22countryCode%22%3A%22IN%22%2C%22ccode3%22%3A%22IND%22%2C%22timezone%22%3A%22Asia%2FCalcutta%22%2C%22ip%22%3A%222406%3A8800%3A9015%3Ac550%3Aeca6%3A44f2%3Affeb%3A2379%22%2C%22regionId%22%3A%22KL%22%2C%22regionName%22%3A%22Kerala%22%7D; __gads=ID=faa1e9087fd1c078:T=1712677321:RT=1735215885:S=ALNI_Ma6L5CmpnceQeaPqEFWmPNRuYfEgA; __eoi=ID=66fbdc7ff144ff21:T=1729334344:RT=1735215885:S=AA-Afjb4iGP-5-EUcCydc8gEb6xn; FCNEC=%5B%5B%22AKsRol9x49FyUytLneK-aWqxeeEukUZ425IquwX27r3DFzxlG02V8gwuI7p5sl3hzFKyHboZQSSPnnEhh602-Crqx6gGbt92MChSCA9Frm79hVqPUSQsyp2P8LW_z2r7Z1Qvsc--dRqVETlsVsGa26fLK1fIfabuMA%3D%3D%22%5D%5D; _hjSession_2585474=eyJpZCI6IjE0MjE0ZTE1LWUyODctNDE0Yy1hM2RjLTUzZWY1M2EwM2Q0NiIsImMiOjE3MzUyMzc5NDAxMDMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _ga_G0V1WDW9B2=GS1.1.1735237938.8.1.1735237941.0.0.0',
        'priority': 'u=1, i',
        'referer': 'https://www.fotmob.com/leagues/113/overview/league',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'x-mas': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvbGVhZ3Vlcz9pZD0xMTMmY2NvZGUzPUlORCZuZXdVZWZhQnJhY2tldD10cnVlIiwiY29kZSI6MTczNTIzNzk0MTA1OCwiZm9vIjoiZTk2YjYwYTIxIn0sInNpZ25hdHVyZSI6IkJDRERBMkY3MjNBODI3N0FGNERDOTUwNkFDQzcxRjcxIn0=',
    }

    params = {
        'id': f'{id}',
        'ccode3': f'{st.session_state.country}',
        # 'newUefaBracket': 'true',
    }

    response = requests.get('https://www.fotmob.com/api/leagues', params=params, headers=headers)
    det=response.json()
    teams={}
    for i in det['table'][0]['data']['table']['all']:
        print(i['name'], i['id'])
        teams.update({i['name']:i['id']})
    return teams
def get_data_destruct():
    st.session_state.opt1 = None
    st.session_state.leagues = {}
    st.session_state.opt2 = None
    st.session_state.choosen = None
    st.session_state.tid = None
    st.session_state.opt3 = None
    st.session_state.teams = {}
    st.session_state.opt4 = None
    st.session_state.players = {}
    st.session_state.returned = {}
def get_data(type): # player, season, team
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://www.fotmob.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'x-mas': 'eyJib2R5Ijp7InVybCI6Ii9hcGkvYWxsTGVhZ3Vlcz9sb2NhbGU9ZW4mY291bnRyeT1JTkQiLCJjb2RlIjoxNzM1MjE1OTA2NzI2LCJmb28iOiJlOTZiNjBhMjEifSwic2lnbmF0dXJlIjoiNjJBNjFEODA1MzVDMUI0N0EwMjAxRERENUI0NTBGNjAifQ==',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
    }

    params = {
        'locale': 'en',
        'country': st.session_state.get('country', ''),
    }

    # Initialize session state variables if they are not already set
    if 'opt1' not in st.session_state:
        st.session_state.opt1 = None
    if 'leagues' not in st.session_state:
        st.session_state.leagues = {}
    if 'opt2' not in st.session_state:
        st.session_state.opt2 = None
    if 'choosen' not in st.session_state:
        st.session_state.choosen = None
    if 'tid' not in st.session_state:
        st.session_state.tid=None
    if 'opt3' not in st.session_state:
        st.session_state.opt3 = None
    if 'teams' not in st.session_state:
        st.session_state.teams = {}
    if 'opt4' not in st.session_state:
        st.session_state.opt4 = None
    if 'players' not in st.session_state:
        st.session_state.players = {}
    if 'returned' not in st.session_state:
        st.session_state.returned ={}

    # Select league nation if opt1 is None
    if st.session_state.opt1 is None and st.session_state.leagues =={}:
        nations = ["international"]
        response = requests.get('https://www.fotmob.com/api/allLeagues', params=params, headers=headers)

        for country in response.json().get('countries', []):
            nations.append(country['name'])

        opt1 = st.selectbox("Choose league nation", nations,key="nation_selection")

        if st.button("Chosen"):
            st.session_state.opt1 = opt1
            leagues = {}

            # Populate leagues based on the selected nation
            if st.session_state.opt1 == "international":
                for league in response.json().get(st.session_state.opt1, [{}])[0].get('leagues', []):
                    leagues[league["name"]] = league["id"]
            else:
                for country in response.json().get('countries', []):
                    if country['name'] == st.session_state.opt1:
                        for league in country['leagues']:
                            leagues[league['name']] = league['id']

            st.session_state.leagues = leagues
            st.session_state.opt2=None

    # Display league selection if leagues are available
    if st.session_state.leagues and st.session_state.opt2 is None:
        # Select league from available leagues
        selected_league = st.selectbox("Select league", list(st.session_state.leagues.keys()),key="League_select",
                                       index=list(st.session_state.leagues.keys()).index(
                                           st.session_state.opt2) if st.session_state.opt2 else 0)

        # Confirm selection
        if st.button("Confirm"):
            # Store the selected league in session state
            st.session_state.opt2 = selected_league

            # Display confirmation message
            st.write("You have selected:", st.session_state.opt2)
            st.session_state.teams={}
            if type == "league":
                st.session_state.returned = {st.session_state.opt2: st.session_state.leagues[st.session_state.opt2]}
                # return st.session_state.opt2,st.session_state.leagues[st.session_state.opt2]
                return st.session_state.returned
            #st.write("Current session state:", st.session_state)

    # Final display of selected league or prompt
    if st.session_state.opt2 and st.session_state.teams=={}:
        #st.session_state.leagues={}
        st.write("Confirmed League:", st.session_state.opt2, "with ID:",
                 st.session_state.leagues[st.session_state.opt2])
        teams=season_team_extract(st.session_state.leagues[st.session_state.opt2])
        st.session_state.teams = teams
        st.session_state.players={}

        # Display league selection if leagues are available
    if st.session_state.teams and st.session_state.players=={}:
        #st.session_state.leagues={}
        #st.session_state.opt2=None
            # Select league from available leagues
        selected_team = st.selectbox("Select team", list(st.session_state.teams.keys()),key="team_select",
                                           index=list(st.session_state.teams.keys()).index(
                                               st.session_state.opt3) if st.session_state.opt3 else 0)

            # Confirm selection
        if st.button("Sure!",key="sure_1"):
                # Store the selected league in session state
            st.session_state.opt3 = selected_team

                # Display confirmation message
            st.write("Selected team:", st.session_state.opt3,"with tid",st.session_state.teams[st.session_state.opt3])
            if type == "team":
                st.session_state.returned={st.session_state.opt3: st.session_state.teams[st.session_state.opt3]}
                #return st.session_state.opt3, st.session_state.teams[st.session_state.opt3]
                return st.session_state.returned
            st.session_state.players=squad_extract(st.session_state.teams[st.session_state.opt3])
            st.session_state.opt4=None
    if st.session_state.players and st.session_state.opt4 is None:
        #st.session_state.teams={}
        #st.session_state.opt3=None
            # Select league from available leagues
        selected_player = st.selectbox("Select player", list(st.session_state.players.keys()),key="select_player",
                                           index=list(st.session_state.players.keys()).index(
                                               st.session_state.opt4) if st.session_state.opt4 else 0)

            # Confirm selection
        if st.button("Sure!",key='sure_2'):
                # Store the selected league in session state
            st.session_state.opt4 = selected_player

                # Display confirmation message
            st.write("Selected player:", st.session_state.opt4,"with pid",st.session_state.players[st.session_state.opt4])
            if type == "player":
                st.session_state.returned={st.session_state.opt4: st.session_state.players[st.session_state.opt4]}
                #return st.session_state.opt4, st.session_state.players[st.session_state.opt4],st.session_state.opt2,st.session_state.leagues[st.session_state.opt2]
                return st.session_state.returned
            #st.session_state.players=squad_extract(st.session_state.teams[st.session_state.opt3])
def main():
    choice2=st.selectbox("Choose:",["Individual Season Stats","Season Stats Comparison","Player v Player comparison"])
    if st.button("Continue"):
        st.session_state.choice2=choice2
    if st.session_state.choice2=="Individual Season Stats":
        #st.write(st.session_state)
        #get_data_destruct()
        a=get_data("player")
        st.write(a)
        #st.write(st.session_state)
        if st.session_state.returned:
            st.warning("please click 'Finished1' if u want to change options")
            get_season_stats(list(st.session_state.returned.keys())[0],list(st.session_state.returned.values())[0],st.session_state.opt2)
            #get_data_destruct()
        if st.button("Finished1"):
            season_comparison_destruct()
            get_season_stats_destruct()
            get_data_destruct()
        st.write(st.session_state)
    elif st.session_state.choice2=="Season Stats Comparison":
        if st.session_state.opt4:
            get_data_destruct()
        #get_season_stats_destruct()
        b=get_data("league")
        st.write(b)
        st.write(st.session_state)
        #st.write(st.session_state)
        if st.session_state.returned:
            st.warning("please click 'Finished2' if u want to change options")
            season_comparison(list(st.session_state.returned.values())[0])
        if st.button("Finished2"):
            get_season_stats_destruct()
            season_comparison_destruct()
            get_data_destruct()
    st.divider()
if __name__ =="__main__":
    main()