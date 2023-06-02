#Imported packages and modules

from urllib import response
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import random
import math
import sys
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import time

#Accessing data from PlayerIDs.csv

pid  = pd.read_csv('PlayerIDs.csv')

while(True):
    while(True):
        name = str(input('Player Name: '))
        i = 0
        l = []
        m = []
        count = 0
        while(i<pid.shape[0]):
            if name.lower() in str(pid.iat[i, 1]).lower():
                l.append(i)
                m.append(pid.iat[i, 0])
            i+=1

        if len(l) == 0:
            print("No such name exists!")
            continue
        elif len(l) == 1:
            break
        else:
            for j in l:
                print(f'{pid.iat[j, 1]} ({pid.iat[j, 2]}) : {count+1}')
                count+=1
            break

    base_url = 'https://understat.com/player/'
    if(len(m) == 1):
        choice = 1
    else:
        choice = int(input('Enter your choice: '))

    player_id = str(m[choice-1])
    url = base_url+player_id

    res = requests.get(url)
    soup = BeautifulSoup(res.content,'lxml')
    scripts = soup.find_all('script')


    season_choice = input("Enter the season: ")
    value = int(input("Enter the real number of goals scored: "))

    print(f'The graph of {pid.iat[l[choice-1], 1]} for the season {season_choice} is being generated')

    strings = scripts[3].string


    ind_start = strings.index('(')+2
    ind_end = strings.index("')")
    json_data = strings[ind_start:ind_end]
    json_data = json_data.encode('utf8').decode('unicode_escape')
    data = json.loads(json_data)

    xG =[]
    result = []
    situation = []
    season = []


    for index in range(len(data)):
        for key in data[index]:
            if key == 'xG':
                xG.append(data[index][key])
            if key == 'result':
                result.append(data[index][key])
            if key == 'situation':
                situation.append(data[index][key])
            if key == 'season':
                season.append(data[index][key])


    col_names = ['season', 'xG', 'result', 'situation']
    df = pd.DataFrame([season, xG, result, situation], index = col_names)
    df = df.T

    newdf = df[(df.season == season_choice)]


    rows = newdf.shape[0]

    # Running the Simulation
    
    shots = 0
    simulations = []
    while(shots<=10000):
        i=0
        total_goals = 0
        while(i<rows):
            p = (float)(newdf.iat[i, 1])*100000
            goal = random.randint(0, 100000)
            if(goal<p):
                total_goals+=1
            i+=1
        simulations.append(total_goals)
        shots+=1


    simulations.sort()
    
    #Creating the Graph
    
    frequency = Counter(simulations)
    values = list(frequency.keys())
    frequencies = list(frequency.values())

    sorted_integers = sorted(frequency.keys(), key =lambda x: frequency[x])
    cumulative_frequencies = np.cumsum([frequency[key] for key in sorted_integers])
    percentile_index = sorted_integers.index(value)
    percentile = (cumulative_frequencies[percentile_index] / np.sum(list(frequency.values()))) * 100

    plt.bar(values, frequencies)
    target_index = values.index(value)
    plt.bar(values[target_index], frequencies[target_index], color= 'red')

    plt.xlabel('Goals')
    plt.ylabel('Frequency')
    plt.title('Distribution of Simulated Goals')
    plt.suptitle(f'Percentile Ranking of Actual Value: {percentile:.2f}%', fontsize=12, fontweight='bold', y=0.95)


    plt.show()
    response = input('Want to Look For Another Player? (y/n): ')
    if(response == 'n'):
        print("Thanks for using our program!")
        time.sleep(3)
        sys.exit()
    else:
        continue
