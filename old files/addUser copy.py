import json
import os
import time
"""
Account type
0 = Main
1 = Ironman
2 = Hardcore Ironman
3 = Ultimate Ironman
"""

userListPath = './data/userlist.json'

if not os.path.exists('./data'):
    print('Did not find data directory, creating ./data')
    os.makedirs('./data')

try:
    open(userListPath, 'r')
    print('User file exists.')
except:
    print('User file not found, creating one now...')
    f = open(userListPath, 'a')
    f.write(json.dumps({'foo': {"accountType": 0}, 'bar': {"accountType": 1}}, indent=4))
    f.close()
    print('User file created.')



def add(user, level):
    if type(user) != str or type(level) != int:
        print("Incorrect arguments. Usage: add('string', int)")
    else:
        rawUserFileData = open(userListPath, 'r').read()
        jsonUserData = json.loads(rawUserFileData)
        if not user in jsonUserData.keys():
            x = {user: {"accountType": level}}
            
            jsonUserData.update(x)
            f = open(userListPath, 'w')
            f.write(json.dumps(jsonUserData, indent=4))
            print(f'Adding user: {user}, level: {level}')
        else:
            print(f'User [{user}] is already in user list with type [{jsonUserData[user]}]')

add('hilmar', 0)

