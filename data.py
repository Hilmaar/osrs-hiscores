import hiscores
import users
import json
import pprint
import time
pp = pprint.PrettyPrinter(depth=4) # DEBUG


# Returns which levels and XP have gone up since last time stats were written to userstats.json.
def gainz(user):
    newStats = hiscores.getHiscores(user)
    oldStats = users.readStats(user)
    for key in oldStats:
        if newStats[key] > oldStats[key] and not "Rank" in key:
            # TODO: Return a dict with keys and values that have gone up.
            print(f'{user} had {key}: {oldStats[key]}, but now has {key}: {newStats[key]}')

# Returns levels gained since userstats.json was last updated.
def gainedLevels(user):
    newStats = hiscores.getHiscores(user)
    oldStats = users.readStats(user)
    gained = {}
    for key in oldStats:
        if newStats[key] > oldStats[key] and "Level" in key:
            x = {key: {'new': newStats[key], 'old': oldStats[key], 'diff': int(newStats[key])-int(oldStats[key])}}
            gained.update(x)
    return gained

# Returns XP gained since userstats.json was last updated.
def gainedXP(user):
    newStats = hiscores.getHiscores(user)
    oldStats = users.readStats(user)
    gained = {}
    for key in oldStats:
        if newStats[key] > oldStats[key] and "XP" in key:
            x = {key: {'new': newStats[key], 'old': oldStats[key], 'diff': int(newStats[key])-int(oldStats[key])}}
            gained.update(x)
    return gained


#print(gainedXP('ehutt'))
# Temporary function
def printGainedXP(user):
    gained = gainedXP(user)
    x = ''
    for key in gained:
        x += (f'[ {time.strftime("%D - %H:%M:%S", time.localtime())} ] -> {user} gained {gained[key]["diff"]} {key}. (Was {gained[key]["old"]}, now has {gained[key]["new"]})\n')
    return x



