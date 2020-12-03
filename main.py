import requests
import json

#setting the API Key so you dont need to manually type it all the time
apiKeyFile = open('API_Key.txt')
apiKey = apiKeyFile.read()

#Function to get the basic summoner data of a given summoner
def getSummoner(summonerName):
    url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerName + '?api_key=' + apiKey
    response = requests.get(url)
    return response.json()

#Function to get the specific ranked data of a given summoner
def getRankedStats(summonerName):
    pass

if __name__ == '__main__':
    print('Welcome to the RiotGamesHelper by Damjan Petrovic!')
    print(apiKey)
    print(type(apiKey))

