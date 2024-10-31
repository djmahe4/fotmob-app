import time
import math
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib import dates
from datetime import date,timedelta
from datetime import datetime as dt
import datetime
import math
import requests
import os


def plot_biorhythm_chart(combined_points, dates,name, st,cycle_label="Combined"):
  """Plots the biorhythm chart with dates using matplotlib.pyplot."""

  if len(combined_points) != len(dates):
    raise ValueError("Combined points and dates lists must have the same length.")
  #fig,ax=plt.subplots()
  fig=plt.figure(figsize=(10, 6))
  plt.plot(combined_points, label=cycle_label)

  # Customize x-axis labels with numbers (optional)
  plt.xticks(range(len(combined_points)))  # Use data point indices

  # Add dates below the x-axis (optional, adjust spacing as needed)
  plt.xticks(range(len(combined_points)), [d[:5] for d in dates], rotation=0, ha='center', va='bottom', fontsize=6)

  plt.xlabel("Day")  # Adjust label if needed
  plt.ylabel("Biorhythm Level")
  plt.title(f"Biorhythm Chart ({name})")
  plt.legend()
  plt.grid(True)
  plt.tight_layout()  # Adjust spacing to avoid overlapping labels
  #return plt
  #plt.show()
  st.pyplot(fig)

def birth_get(id="4617846"):

    params = {
        'matchId': f'{id}',
    }

    response = requests.get('https://www.fotmob.com/api/matchDetails', params=params)
    gem = response.json()
    hid=gem["general"]['homeTeam']['id']
    aid = gem["general"]['awayTeam']['id']
    ids=[hid,aid]
    #st.write(gem)
    #st.write(ids)
    details={}
    for i in ids:
        params = {
            'id': f'{i}',
            'ccode3': 'IND',
        }

        response = requests.get('https://www.fotmob.com/api/teams', params=params)
        gem = response.json()
        #st.write(gem)
        sortedl=gem["squad"][1:]
        #st.write(sortedl)
        for j in sortedl:
            #st.write(j)
            #exit(0)
            #st.write(j)
            #exit(0)
            for k in j['members']:
                #st.write(k)
                name=k['name']
                pid=k['id']
                params = {
                    'id': f'{pid}',
                }

                response = requests.get('https://www.fotmob.com/api/playerData', params=params)
                gem = response.json()
                dob=gem["birthDate"]["utcTime"]
                details.update({name:dob})
                #time.sleep(2)
                #break
        #break
    #st.write(details)
    return details


def usedata(name,n):
    for i in range(len(n)):
        if name in n[i]:
           # st.write("Name of the player:", n[i])
            pname=n[i]
            dob= n[i+1]
            sr=""
            form_dob=dob.split("/")[::-1]
            for i in form_dob:
                sr+=i+"-"
            return sr[:-1],pname

def days_since_birth(date_of_birth):
    """Calculates the number of days since birth considering leap years"""
    today = date.today()
    # Extract year, month, day from the provided date of birth string
    #date_str = "1995-10-19T00:00:00.000Z"

    # Parse the date string into a datetime object
    date_obj = dt.strptime(date_of_birth, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Extract the year, month, and day
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day

    # Create a date object representing the date of birth
    birth_date = date(year, month, day)

    # Calculate the difference between today and date of birth in days
    time_delta = today - birth_date
    return time_delta.days


def calculate_bhagyank(date_of_birth):
    """Calculates Bhagyank from date of birth"""
    date_obj = dt.strptime(date_of_birth, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Extract the year, month, and day
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    sum = 0
    for i in str(day):
        sum = sum + int(i)
    if sum > 9:
        sum1 = 0
        for i in str(sum):
            sum1 = sum1 + int(i)
        sum = sum1
    for i in str(month):
        sum = sum + int(i)
    if sum > 9:
        sum2 = 0
        for i in str(sum):
            sum2 = sum2 + int(i)
        sum = sum2
    for i in str(year):
        sum = sum + int(i)
    if sum > 9:
        sum3 = 0
        for i in str(sum):
            sum3 = sum3 + int(i)
        sum = sum3
    if sum > 9:
        sum4 = 0
        for i in str(sum):
            sum4 = sum4 + int(i)
        sum = sum4
    return sum
    # return (day + month + (year % 100) + (year // 100)) % 9 + 1  # Ensure Bhagyank is 1-9


def calculate_naamank(name):
    aldict = {'a': 1, 'j': 1, 's': 1, 'b': 2, 'k': 2, 't': 2, 'c': 3, 'l': 3, 'u': 3, 'd': 4, 'm': 4, 'v': 4, 'e': 5, 'n': 5, 'w': 5, 'f': 6, 'o': 6, 'x': 6, 'g': 7, 'p': 7, 'y': 7, 'h': 8, 'q': 8, 'z': 8, 'i': 9, 'r': 9}
    """Calculates Naamank (sum of numerological letter values)"""
    name_sum = 0
    for letter in name.lower().strip():
        if letter != " ":
            number = aldict.get(letter, 0)  # Initialize number with 0 if letter not found
            name_sum += number

    while name_sum > 9:
        sum_digits = 0
        for digit in str(name_sum):
            sum_digits += int(digit)
        name_sum = sum_digits
    if name_sum +3>9:
      name_sum=name_sum-3
    else:
      name_sum=name_sum+3
    return name_sum
def calculate_moolank(date_of_birth):
  """Calculates Moolank from date of birth"""
  date_obj = dt.strptime(date_of_birth, "%Y-%m-%dT%H:%M:%S.%fZ")

  # Extract the year, month, and day
  day = date_obj.day
  sum=0
  for i in str(day):
    sum=sum+int(i)
  if sum>9:
      sum1 = 0
      for i in str(sum):
          sum1 = sum1 + int(i)
      sum=sum1
  #return sum
  return sum

def combine_numbers( moolank,bhagyank, naamank,st):
    """Combines Moolank, Bhagyank, and Naamank with Fibonacci offset (not scientific)"""
    #combined = (moolank * 3 + bhagyank * 2 + normalized_naamank)  # / 6
    #combined= moolank+(bhagyank*naamank)
    combined = bhagyank + (moolank * naamank)
    #print('{}*{}+{}={}'.format(bhagyank, naamank, moolank, combined))
    print('{}+({}*{})={}'.format(bhagyank, moolank,naamank, combined))
    st.write('{}+({}*{})={}'.format(bhagyank, moolank,naamank, combined))
    typ= +9.81
    #if combined<=9:
            #combined = bhagyank * naamank
            #print("Alternate {}*{}={}".format(bhagyank,naamank,combined))
        #combined = moolank + (bhagyank * naamank)
        #print('{}*{}+{}={}'.format(bhagyank, naamank, moolank, combined))
        #typ= -9.81
    return combined ,typ
#if moolank> else ValueError # - fibonacci_offset, fibonacci_sequence


def biorhythm_chart(days, combined):
    """Generates biorhythm chart using Fibonacci sequences (not scientific)"""
    biorhythm_data = []
    # for cycle, factor in zip(cycles, fibonacci_scaling_factors):
    # fibonacci_values = [f * factor for f in fibonacci_sequence[:cycle]]
    biorhythm_data.append([math.sin(2 * math.pi * i / combined) for i in range(days - 15, days + 15)])

    return biorhythm_data[0]
def get_date_range(days_before=15, days_after=14):
  """
  Finds today's date and a range of dates before and after in dd-mm-yyyy format.

  Args:
      days_before (int, optional): Number of days before today (default: 15).
      days_after (int, optional): Number of days after today (default: 14).

  Returns:
      list: A list of strings representing the dates in dd-mm-yyyy format.
  """
  today = date.today()
  date_range = []

  # Add date 15 days before today
  #date_range.append(today - timedelta(days=days_before))
  for i in range(-15, days_after +1):
    date_range.append(today - timedelta(days=i))
  formatted_dates = [date.strftime("%d-%m-%Y") for date in date_range]

  return formatted_dates

def main(id,st):
    #with open("data.txt", "r") as f:
        #x = f.read()
        #n = x.split()
    # Get the date range
    date_list = get_date_range()
    matchid=id
    #date_of_birth,name=usedata(y,n)
    data=birth_get(matchid)
    for name, date_of_birth in data.items():
        st.write(f"Name: {name}")
        st.write(f"DOB: {date_of_birth}")
        #st.write(bd)
        bhagyank = calculate_bhagyank(date_of_birth)
        moolank = calculate_moolank(date_of_birth)
        naamank = calculate_naamank(name)

        st.write(f"Bhagyank: {bhagyank}")
        st.write(f"Naamank: {naamank}")
        st.write("Moolank:",moolank)
        # Biorhythm chart parameters (adjust as needed)
        # cycles = [23, 28, 33]  # Physical,
        comb,typ = combine_numbers( moolank,bhagyank, naamank,st)
        days = days_since_birth(date_of_birth)
        bio = biorhythm_chart(days,comb)
        di={}
        for i,date in enumerate(date_list):
            di.update({date:bio[i]})
        #st.write(di)
        # st.write table header
        st.write("-" * 58)
        new = pd.DataFrame(di.items(), columns=["Date", "Values"])
        st.table(new)
        #plot_biorhythm_chart(bio, date_list)
        ck=16 #ck should be set to 15 by default
        if abs(float(f"{bio[ck - 1]:.4f}")) == abs(float(f"{bio[ck + 1]:.4f}")):
            st.write("Warning!! Prediction may fail!")
        #st.write(bio)
        ls=[abs(round(ele,4)) for ele in bio[:-(30-ck+1):-1]]
        #st.write(ls)
        mx=max(ls)
        ln=0
        found=False
        while ln < len(ls):
            last = ls[ln]
            try:
                if ls[ln - 1] == mx and ln >= 0:
                    found = True
                    # ln += 1
                    # continue
                elif ls[ln + 1] == mx:
                    found = True
                    # ln += 2
                    # continue
                    ln += 1
            except IndexError:
                st.write("Passed {}".format(ls[ln]))
                # pass
            if ls[ln] == mx:
                found = True
                # ln+=1
                # continue
            if found:
                st.write(ls[ln])
                ln = ln + 2
            else:
                st.write("Not found {}".format(ls[ln]))
                ln = ln + 1

        if last == ls[-1]:
            st.write("Great..")
        else:
            st.write("Flop :(")
        for i in ls[-4:]:
            if ls[-4:].count(i) > 1:
                st.write("Pipe!")
                break
        plot_biorhythm_chart(list(di.values()),list(di.keys()),name,st)
        st.write("-"*58)
        st.write("-" * 58)
        #save_plt(plt,matchid,name)



    #birth_get()