import requests
import os
skillListFile = './data/hiscorelist.txt'
seperatedSkillListFile = './data/hiscorelistSeperated.txt'
apiUrl = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player='

def getSkillList(): #Reads a list of skills in the correct order given from the OSRS Hiscores API.
    with open(skillListFile) as file:
        skillListRaw = file.read().split('\n')
    skillList = []
    for line in skillListRaw:
        skillList.append(line)
    return skillList

def getSeperatedSkillList(): #Reads a list of skills in the correct order given from the OSRS Hiscores API.
    with open(seperatedSkillListFile) as file:
        seperatedSkillListRaw = file.read().split('\n')
    seperatedSkillList = []
    for line in seperatedSkillListRaw:
        seperatedSkillList.append(line)
    return seperatedSkillList
    
def getApi(user): #Returns data as a 2d array, in the order found in ./hiscorelist.txt, ['rank', 'level', 'xp'].
    if type(user) == str:
        response = requests.get(apiUrl+user).text.split('\n')
        skillSplit = []
        for line in response:
            split = line.split(',')
            skillSplit.append(split)
        return skillSplit
    else:
        print(f'{user} is {type(user)}, expecting a string.')
        return 'Error'


def getRank(user): #Returns a dict with the users' ranks. Keys being name of a skill and value the rank.
    userRank = {}
    i = 0
    for line in getSkillList():
        userRank.update({line: getApi(user)[i][0]})
        i = i + 1
    return userRank

def getLevel(user): #Returns a dict with the users' levels. Keys being name of a skill and value the level.
    userLevel = {}
    i = 0
    for line in getSkillList():
        userLevel.update({line: getApi(user)[i][1]})
        i = i + 1
    return userLevel

def getXp(user): #Returns a dict with the users' xp. Keys being name of a skill and value the xp.
    userXp = {}
    i = 0
    for line in getSkillList():
        userXp.update({line: getApi(user)[i][2]})
        i = i + 1
    return userXp





# Returns a dict with the users' Rank, level and XP.
# For example: 
# {'overallRank': '719226', 'overallLevel': '1631', 'overallXP': '25527953', 'attackRank': '878352', 'attackLevel': '78', 'attackXP': '1639593'}
# getHiscores('Username')['attackLevel'] will return 78.
def getHiscores(user):
    userHiscores = {}
    skillSplit = getApi(user)
    i = 0
    for line in getSeperatedSkillList()[0::3]:
        userHiscores.update({line: int(skillSplit[i][0])})
        i = i + 1
    i = 0
    for line in getSeperatedSkillList()[1::3]:
        userHiscores.update({line: int(skillSplit[i][1])})
        i = i + 1
    i = 0
    for line in getSeperatedSkillList()[2::3]:
        userHiscores.update({line: int(skillSplit[i][2])})
        i = i + 1
    return userHiscores







