import tomli
import tomli_w
configFile = './config.toml'
defaultConfig = {
    'paths': {
        'dataDir': './data/',
        'userDataDir': './data/userdata/',
        'userListPath': './data/userlist.json',
        'userStatsPath': './data/userstats.json',
        'historicUserStatsPath': './data/userdata/'
    },

    'discord': {
        'token': 'token_go_here',
        'ownedId': '0123456789'
    }
}


def createConfig():
    try:
        with open('./config.toml', 'r') as file:
            pass
        print(f"Config file found at ./config.toml")

    except:
        print(f"Config file not found, creating config file ./config.toml")
        with open('./config.toml', 'wb') as file:
            tomli_w.dump(defaultConfig, file)


def checkConfig():
    try:
        with open(configFile, 'rb') as file:
            tomli.load(file)
        return True
    except:
        raise Exception('TOML Config parsing error. Fix errors in config.toml, or delete it to generate a new config file.')


def readConfig():
    try:
        with open(configFile, 'rb') as file:
            config = tomli.load(file)
        return config
    except FileNotFoundError:
        createConfig()
        with open(configFile, 'rb') as file:
            config = tomli.load(file)
        return config
    finally:
        checkConfig()