from statistics import median

import requests

apiKeyFile = open('API_Key.txt')
apiKey = apiKeyFile.read()

def getSummoner(summonerName):
    url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + apiKey
    response = requests.get(url)
    return response.json()

def getMatchHistory(summonerName):
    customerData = getSummoner(summonerName)
    accountId = customerData["accountId"]
    url = 'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + accountId + '?endIndex=50&api_key=' + apiKey
    response = requests.get(url)
    return response.json()

def getMatchStats(matchId):
    url = "https://euw1.api.riotgames.com/lol/match/v4/matches/" + str(matchId) + "?api_key=" + apiKey
    response = requests.get(url)
    return response.json()

def getMedian(list):
    return median(list)


games = []
championId = []
championsPlayed = []
kills = []
deaths = []
assists = []
totalDamageDealt = []
visionScore = []

matchHistory = getMatchHistory(summonerNames[y])
for each in matchHistory["matches"]:
    games.append(each["gameId"])
    championsPlayed.append(each["champion"])

for z in range(0, 20):
    matchData = getMatchStats(games[z])
    for part in matchData["participants"]:
        if part["championId"] == championsPlayed[z]:
            championId.append(part["championId"])
            kills.append(part["stats"]["kills"])
            deaths.append(part["stats"]["deaths"])
            assists.append(part["stats"]["assists"])
            totalDamageDealt.append(part["stats"]["totalDamageDealtToChampions"])
            visionScore.append(part["stats"]["visionScore"])

# print(games)
# print(championId)
print("KDA: " + str(getMedian(kills)) + " /" + str(getMedian(deaths)) + " / " + str(getMedian(assists)))
print("Damage dealt to Champions: " + str(getMedian(totalDamageDealt)))
print("Vision Score: " + str(getMedian(visionScore)) + "\n")