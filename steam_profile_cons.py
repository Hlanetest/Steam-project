#For handiling the API calls to pull user data
import requests
import json
class handler():
    def __init__(self, steamid):
        self.steamid = steamid
    def get_game_id(self):
        '''Talks to the steam API, fetches the game IDS, as well as user playtime for said games. stores arrays into appIdList & playTimeList'''
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}=json".format(self.steamid)
        html_content = requests.get(url)
        json_response = json.loads(html_content.text)
        appIdList = [x["appid"] for x in json_response["response"]["games"]]
        playTimeList = [x["playtime_forever"] for x in json_response["response"]["games"]]        
        return appIdList, playTimeList

    def get_user_profile(self):
        '''Talks to the steam API, fetches user profiles. Stores array into username variable'''    
        profile_url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}".format(self.steamid)
        user_content = requests.get(profile_url)
        user_response = json.loads(user_content.text)
        username = [x["personaname"] for x in  user_response["response"]["players"]]
        return username


