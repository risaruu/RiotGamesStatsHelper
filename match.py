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
    url = 'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + accountId + '?endIndex=20&api_key=' + apiKey
    response = requests.get(url)
    return response.json()

def getMatchStats(matchId):
    url = "https://euw1.api.riotgames.com/lol/match/v4/matches/" + str(matchId) + "?api_key=" + apiKey
    response = requests.get(url)
    return response.json()

games = []
championId = []
championsPlayed = []
kills = []
deaths = []
assists = []
totalDamageDealt = []
visionScore = []

matchHistory = getMatchHistory('lebenistleiden')
for each in matchHistory["matches"]:
    games.append(each["gameId"])
    championsPlayed.append(each["champion"])

for x in range(0, 20):
    matchData = getMatchStats(games[x])
    for part in matchData["participants"]:
        if part["championId"] == championsPlayed[x]:
            championId.append(part["championId"])
            kills.append(part["stats"]["kills"])
            deaths.append(part["stats"]["deaths"])
            assists.append(part["stats"]["assists"])
            totalDamageDealt.append(part["stats"]["totalDamageDealtToChampions"])
            visionScore.append(part["stats"]["visionScore"])

print(games)
print(championId)
print(kills)
print(deaths)
print(assists)
print(totalDamageDealt)
print(visionScore)