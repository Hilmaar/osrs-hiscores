import json
import os
import time
import hiscores
"""
Account type
0 = Main
1 = Ironman
2 = Hardcore Ironman
3 = Ultimate Ironman
"""
userListPath = './data/userlist.json'
userStatsPath = './data/userstats.json'
historicUserStatsPath = './data/userdata/'

if not os.path.exists('./data/userdata'):
    print('Did not find data directory, creating ./data/userdata')
    os.makedirs('./data/userdata')


def add(user, level):
    if type(user) != str or type(level) != int:
        print("Incorrect arguments. Usage: add('string', int)")
    else:
        x = {user: {"accountType": level}}
        try:
            with open(userListPath, 'r') as file:
                rawUserFileData = file.read()
                jsonUserData = json.loads(rawUserFileData)
                if not user in jsonUserData.keys():
                    jsonUserData.update(x)
                    with open(userListPath, 'w') as file:
                        file.write(json.dumps(jsonUserData, indent=4))
                    print(f'Adding user {user} with account type {level}.')
                else:
                    print(f'User {user} already exists.')
        except:
            with open(userListPath, 'w') as file:
                file.write(json.dumps(x, indent=4))
                print(f'Userfile not found, creating user file and adding user {user} with account type {level}')
                

def writeStats(user):
    userStats = hiscores.getHiscores(user)
    x = {user: userStats}
    try:
        with open(userStatsPath, 'r') as file:
            fileData = file.read()
            jsonData = json.loads(fileData)
            jsonData.update(x)
        with open(userStatsPath, 'w') as file:
            file.write(json.dumps(jsonData, indent=4))
        print(f'Adding stats for {user} to {userStatsPath}')
    except:
        with open(userStatsPath, 'w') as file:
            file.write(json.dumps(x, indent=4))
            print(f'Did not find userstats file, creating {userStatsPath} and adding {user} to file.')


def saveHistoricData(user):
    userDataDir = historicUserStatsPath+user
    if not os.path.exists(userDataDir):
        print(f'Did not find directory for user {user}, creating {userDataDir}.')
        os.makedirs(userDataDir)
    timestamp = str(int(time.time()))
    filename = user+'-'+timestamp+'.json'
    filepath = userDataDir+'/'+filename
    userStats = hiscores.getHiscores(user)
    x = {user: userStats}
    with open(filepath, 'w') as file:
        file.write(json.dumps(x, indent=4))
    print(f'Wrote data for user {user} at {filepath}.')

def removeOldHistoricData(user, length): # length represents time since creation of file in minutes.
    userDataDir = historicUserStatsPath+user
    ageLength = length * 60 # Function input takes minutes, time is stored as unixtime (seconds.)

    if not os.path.exists(userDataDir):
        print(f'Did not find a directory containing historic data for user {user}.')
    else:
        files = os.listdir(userDataDir)
        filelist = []
        for file in files:
            a = file.split('-')
            b = a[1].split('.')
            filelist.append(int((b[0])))
        fileAge = {}
        timeNow = int(time.time())
        for file in filelist:
            ageOfFile = round((timeNow - file))
            fileAge[file] = ageOfFile
        deletingFiles = ''
        for file in fileAge:
            if fileAge[file] >= ageLength:
                fileName = user+'-'+str(file)+'.json'
                #os.remove(userDataDir+'/'+fileName)
                deletingFiles += fileName+', '
                
        if len(deletingFiles) > 10:
            print(f'Deleting files: {deletingFiles[:-2]}.')
        else:
            print(f'No files were older than {length} minutes.')
