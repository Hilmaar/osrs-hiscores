import users
import hiscores
import time
import config
import data

while True:
    names = users.getAllUsers()
    for user in names:
        #print(time.strftime("%D - %H:%M:%S", time.localtime()))
        x = data.printGainedXP(user)
        if x != '':
            print(x)
        with open('./log.txt', 'a') as file:
            file.write(x)
        users.writeStats(user)
    time.sleep(600)