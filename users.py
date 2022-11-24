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

writeStats('hilmar')
writeStats('ehutt')

