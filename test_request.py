import requests
from bs4 import BeautifulSoup
import steam_profile_cons
import json


steamid = input("Enter steam ID:")
api_key = input("enter your API key:")
handle = steam_profile_cons.handler(api_key, steamid)
game_id = handle.get_game_id()


class var_builder():
    def __init__(self, game_id):
        self.game_id = game_id

    def json_builder(self):
        '''The main driver that checks all the steam apps based upon appID and stores them into a Json array, along with the release date, recent, all reviews, and titles'''
        for i in game_id:
            try:
                url = "https://store.steampowered.com/app/{}".format(i)
                html_content = requests.get(url).text
                soup = BeautifulSoup(html_content, 'lxml')
                title = soup.title.text

                if title == "Welcome to Steam":
                    pass

                try:
                    recent_review = soup.find(
                        'span', class_="game_review_summary positive").text
                except AttributeError:
                    print(i, "Game {} has no recent reviews".format(
                        title.replace('on Steam', '')))
                all_review = soup.find(
                    'span', attrs={'itemprop': 'description'}).text
                release_date = soup.find(
                    'div', class_='release_date').text.replace("\nRelease Date:\n", "").replace("\n", "")
                game_id[i]['name'] = title.replace('on Steam', '')
                game_id[i]['release_date'] = release_date
                game_id[i]['recent_score'] = recent_review
                game_id[i]['total_score'] = all_review
            except AttributeError:
                print("unable to find store page. ", i)
        print(json.dumps(game_id, indent=2))


var_builder.json_builder(game_id)
