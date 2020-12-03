import requests
import Summoner

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

def calculateWinrate(x, y):
    z = x + y
    z_formatted = round(x / z * 100, 2)
    return str(z_formatted)

def getMatchHistory(summonerName):
    customerData = getSummoner(summonerName)
    accountId = customerData["accountId"]
    url = 'https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + accountId + '?api_key=' + apiKey
    response = requests.get()
    return response.json()

if __name__ == '__main__':
    #Printing out a welcoming message
    print('Welcome to the RiotGamesHelper by Damjan Petrovic!')

    #summonerName = input('Gib eine den Summoner Name: ')
    summonerName = "dasammadabei"

    summonerData = getSummoner(summonerName)
    summonerDataRanked = getRankedStats(summonerName)

    print(summonerData["id"])
    print(summonerData["puuid"])
    print(summonerData["accountId"] + "\n\n")

    print(summonerData["name"] + " ist gerade Lv." + str(summonerData["summonerLevel"]))
    if summonerDataRanked[0]["queueType"] == "RANKED_SOLO_5x5":
        print("Stats für Ranked Solo/Duo")
    elif summonerDataRanked[0]["queueType"] == "RANKED_FLEX_SR":
        print("Stats für Ranked Flex")
    print("Tier: " + summonerDataRanked[0]["tier"] + " " + summonerDataRanked[0]["rank"])
    print("Winrate beträgt: " + calculateWinrate(summonerDataRanked[0]["wins"], summonerDataRanked[0]["losses"]))
