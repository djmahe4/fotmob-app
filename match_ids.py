import requests
from datetime import date
import json

def get_match_ids():
    x=date.today()
    y=str(x).split('-')
    z=''
    for i in y:
        z=z+i

    params = {
        'date': f'{z}',
        'timezone': 'Asia/Calcutta',
        'ccode3': 'IND',
    }
    response = requests.get('https://www.fotmob.com/api/matches', params=params)#, cookies=cookies, headers=headers)
    yes=response.json()

    a=yes["leagues"]
    b=[]
    for i in a:
        #print(i.keys())
        c=[i['name'],i['matches']]
        leagueid=i['id']
        matches=[]
        for x in i['matches']:
            score=[]
            matchid=x['id']
            d=x['home']
            hname=d['longName']
            score.append(d['score'])
            e=x['away']
            aname=e['longName']
            score.append(e['score'])
            teams=[hname,aname]
            matches.append({matchid:[teams,score]})
        #b.append({"date":date.today()})
        b.append({leagueid:matches})
        with open("leagues.json",'w',encoding='utf-8') as file:
            #obj=json.load(open("leagues.json"))
            #obj["date"]=date.today()
            json.dump(b, file, indent=2,ensure_ascii=False)
    file.close()
get_match_ids()