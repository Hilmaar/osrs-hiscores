import json
import os
import hiscores
"""
Account type
0 = Main
1 = Ironman
2 = Hardcore Ironman
3 = Ultimate Ironman
"""
userListPath = './data/userlist.json'
userStatsPata = './data/userstats.json'

if not os.path.exists('./data'):
    print('Did not find data directory, creating ./data')
    os.makedirs('./data')



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
                
                
