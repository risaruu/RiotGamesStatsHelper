import requests
import re
from statistics import median

#setting the API Key from a file to not always type it in manually
apiKeyFile = open('API_Key.txt')
apiKey = apiKeyFile.read()

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

#Function to simply calculate the winrate out of the wins and losses of an Account
def calculateWinrate(x, y):
    z = x + y
    z_formatted = round(x / z * 100, 2)
    return str(z_formatted)

def getMatchHistory(summonerName):
    customerData = getSummoner(summonerName)
    accountId = customerData["accountId"]
    url = 'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + accountId + '?endIndex=10&api_key=' + apiKey
    response = requests.get(url)
    return response.json()

def getMatchStats(matchId):
    url = "https://euw1.api.riotgames.com/lol/match/v4/matches/" + str(matchId) + "?api_key=" + apiKey
    response = requests.get(url)
    return response.json()

def getMedian(list):
    return median(list)

#Function to make multiple line inputs possible and also reformat the input into just a list of the usernames
def getUserInput():
    lines = ""
    for i in range(5):
        lines += input()

    text = re.findall(r'.+?joined the lobby', lines)
    for x in range(5):
        text[x] = text[x].replace("joined the lobby", "")
        text[x] = text[x].replace(" ", "")
    return text

def clearLists():
    games.clear()
    championId.clear()
    championsPlayed.clear()
    kills.clear()
    deaths.clear()
    assists.clear()
    totalDamageDealt.clear()
    visionScore.clear()

if __name__ == '__main__':
    #Printing out a welcoming message
    print('Welcome to the RiotGamesHelper by Damjan Petrovic!')

    summonerNames = getUserInput()
    games = []
    championId = []
    championsPlayed = []
    kills = []
    deaths = []
    assists = []
    totalDamageDealt = []
    visionScore = []

    #doing this one time for every Summoner in your team so 5 times
    for y in range(5):
        summonerData = getSummoner(summonerNames[y])
        summonerDataRanked = getRankedStats(summonerNames[y])

        print(summonerData["name"] + " ist gerade Lv." + str(summonerData["summonerLevel"]))
        try:
            if summonerDataRanked[0]["queueType"] == "RANKED_SOLO_5x5":
                print("Stats für Ranked Solo/Duo")
                print("Tier: " + summonerDataRanked[0]["tier"] + " " + summonerDataRanked[0]["rank"])
                print("Winrate beträgt: " + calculateWinrate(summonerDataRanked[0]["wins"], summonerDataRanked[0]["losses"]))
            elif summonerDataRanked[0]["queueType"] != "RANKED_SOLO_5x5":
                print("Stats für Ranked Solo/Duo")
                print("Tier: " + summonerDataRanked[1]["tier"] + " " + summonerDataRanked[1]["rank"])
                print("Winrate beträgt: " + calculateWinrate(summonerDataRanked[1]["wins"], summonerDataRanked[1]["losses"]))
        except:
            print("Summoner hat keine Ranked Games gespielt.")

        #gettint the match history and creating a list of the champions played to later get specific stats out of the match stats
        matchHistory = getMatchHistory(summonerNames[y])
        for each in matchHistory["matches"]:
            games.append(each["gameId"])
            championsPlayed.append(each["champion"])

        for z in range(0, 10):
            matchData = getMatchStats(games[z])
            for part in matchData["participants"]:
                if part["championId"] == championsPlayed[z]:
                    championId.append(part["championId"])
                    kills.append(part["stats"]["kills"])
                    deaths.append(part["stats"]["deaths"])
                    assists.append(part["stats"]["assists"])
                    totalDamageDealt.append(part["stats"]["totalDamageDealtToChampions"])
                    visionScore.append(part["stats"]["visionScore"])

        print("KDA: " + str(getMedian(kills)) + " /" + str(getMedian(deaths)) + " / " + str(getMedian(assists)))
        print("Damage dealt to Champions: " + str(getMedian(totalDamageDealt)))
        print("Vision Score: " + str(getMedian(visionScore)) + "\n")

        print("ID:" + summonerData["id"])
        print("Puuid" + summonerData["puuid"])
        print("AccountID" + summonerData["accountId"] + "\n\n")

        clearLists()
