import requests
import os

hiscorelistfile = './hiscorelist.txt'
with open(hiscorelistfile) as file:
    hiscorelistdata = file.read().split('\n')

hiscorelistList = []
for line in hiscorelistdata:
    hiscorelistList.append(line)

player = 'hilmar'
api_url = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player='+player
response = requests.get(api_url).text
skills = []
splitResponse = response.split('\n')


skillSplit = []
for line in splitResponse:
    split = line.split(',')
    skillSplit.append(split)

i = 0
userRank = {}
userLevel = {}
userXP = {}
for line in hiscorelistList:
    try:
        userRank.update({line: skillSplit[i][0]})
        i = i + 1
    except IndexError:
        if not i == 24:
            print("Something went wrong")
i = 0
for line in hiscorelistList:
    try:
        userLevel.update({line: skillSplit[i][1]})
        i = i + 1
    except IndexError:
        if not i == 24:
            print("Something went wrong")
i = 0
for line in hiscorelistList:
    try:
        userXP.update({line: skillSplit[i][2]})
        i = i + 1
    except IndexError:
        if not i == 24:
            print("Something went wrong")






