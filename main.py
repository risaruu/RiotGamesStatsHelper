import requests
import re
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

#Function to simply calculate the winrate out of the wins and losses of an Account
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


if __name__ == '__main__':
    #Printing out a welcoming message
    print('Welcome to the RiotGamesHelper by Damjan Petrovic!')

    #summonerName = input('Gib eine den Summoner Name: ')
    summonerNames = getUserInput()

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

        print("ID:" + summonerData["id"])
        print("Puuid" + summonerData["puuid"])
        print("AccountID" + summonerData["accountId"] + "\n\n")
