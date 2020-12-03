import requests
import json

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

if __name__ == '__main__':
    #Printing out a welcoming message
    print('Welcome to the RiotGamesHelper by Damjan Petrovic!')

    summonerName = input('Gib eine den Summoner Name: ')
    summonerData = getSummoner(summonerName)
    summonerDataRanked = getRankedStats(summonerName)

    print(summonerData["name"] + " ist gerade Lv." + str(summonerData["summonerLevel"]))
    print("Tier: " + summonerDataRanked[0]["tier"] + " " + summonerDataRanked[0]["rank"])
