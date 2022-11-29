import hiscores
import users
import json


# Returns which levels and XP have gone up since last time stats were written to userstats.json.
def gainz(user):
    newStats = hiscores.getHiscores(user)
    oldStats = users.readStats(user)
    for key in oldStats:
        if newStats[key] > oldStats[key] and not "Rank" in key:
            # TODO: Return a dict with keys and values that have gone up.
            print(f'{user} had {key}: {oldStats[key]}, but now has {key}: {newStats[key]}')

