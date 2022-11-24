import json
import os
"""
User "Levels"
0 = Main
1 = Ironman
2 = Hardcore Ironman
3 = Ultimate Ironman
"""

userListPath = './data/userlist.txt'

if not os.path.exists('./data'):
    print('Did not find data directory, creating ./data')
    os.makedirs('./data')

try:
    open(userListPath, 'r')
    print('User file found.')
except:
    print('User file not found, creating one now...')
    open(userListPath, 'x')
    print('User file created.')
    f = open(userListPath, 'a')
    x = {'hilmar': 0}
    f.write(x)




def add(user, level):
    if not type(user) == str and not type(level) == int:
        print("Incorrect arguments. Use add('string', int")
    else:
        print('User: '+user+', level: '+str(level))
        userData = open(userListPath, 'r').read()
        x = {user: level}
        updatedUserData = updatedUserData.update(x)
        f = open(userListPath, 'w')
        f.write(updatedUserData)

add('orri', '0')