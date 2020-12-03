import requests

#setting the API Key from a file to not always type it in manually
apiKeyFile = open('API_Key.txt')
apiKey = apiKeyFile.read()

#Variablen
name = "default_Name"
queueType = "default_queue_type"
wins = 0
losses = 0
lvl = 0
tier = "hiniger"
rank = "rank"

#Function to get the basic summoner data of a given summoner
def getSummoner(summonerName):
    url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + apiKey
    response = requests.get(url)
    return response.json()

#Function to get the specific ranked data of a given summoner
def getRankedStats(summonerName):
    customerData = getSummoner(summonerName)
    summonerId = customerData["id"]
    url = 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + summonerId + '?api_key=' + apiKey
    response = requests.get(url)
    return response.json()

def calculateWinrate(x, y):
    z = x + y
    z_formatted = round(x / z * 100, 2)
    return str(z_formatted)

def variablenSetzen():
    pass

if __name__ == '__main__':
    #Printing out a welcoming message
    print('Welcome to the RiotGamesHelper by Damjan Petrovic!')

    #summonerName = input('Gib eine den Summoner Name: ')
    summonerName = "athelesia"
    summonerData = getSummoner(summonerName)
    summonerDataRanked = getRankedStats(summonerName)

    print(summonerData["id"])
    print(summonerDataRanked[1]["queueType"])
    print(summonerData["name"] + " ist gerade Lv." + str(summonerData["summonerLevel"]))
    print(summonerDataRanked[1]["queueType"])
    print("Tier: " + summonerDataRanked[1]["tier"] + " " + summonerDataRanked[1]["rank"])
    print("Seine Winrate beträgt: " + calculateWinrate(summonerDataRanked[1]["wins"], summonerDataRanked[1]["losses"]))
