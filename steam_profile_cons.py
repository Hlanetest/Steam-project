#For handiling the API calls to pull user data
import requests
import json


class handler():
    def __init__(self, steamid, api_key):
        self.steamid = steamid
        self.api_key = api_key
    def get_game_id(self):
        '''Talks to the steam API, fetches the game IDS, as well as user playtime for said games. stores arrays into appIdList & playTimeList'''
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}=json".format(self.steamid, self.api_key)
        html_content = requests.get(url)
        json_response = json.loads(html_content.text)
        appIdList = [x["appid"] for x in json_response["response"]["games"]]   
        return appIdList
    
    def get_game_time(self):
        '''Pulls the playtime of all the games on the specified users profile'''
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}=json".format(self.steamid, self.api_key)
        html_content = requests.get(url)
        json_response = json.loads(html_content.text)
        playTimeList = [x["playtime_forever"] for x in json_response["response"]["games"]] 
        return playTimeList

    def get_user_profile(self):
        '''Talks to the steam API, fetches user profiles. Stores array into username variable'''    
        profile_url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}".format(self.steamid, self.api_key,)
        user_content = requests.get(profile_url)
        user_response = json.loads(user_content.text)
        username = [x["personaname"] for x in  user_response["response"]["players"]]
        return username


