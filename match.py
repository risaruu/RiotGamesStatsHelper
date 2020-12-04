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
matchHistory = getMatchHistory('lebenistleiden')
for each in matchHistory["matches"]:
    games.append(each["gameId"])
    championsPlayed.append(each["champion"])

for x in range(0, 20):
    matchData = getMatchStats(games[x])
    for part in matchData["participants"]:
        if part["championId"] == championsPlayed[x]:
            championId.append(part["championId"])

print(games)
print(championId)