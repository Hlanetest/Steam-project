import requests
from bs4 import BeautifulSoup
import steam_profile_cons


steamid = input("Enter steam ID:")
api_key = input("enter your API key:")
handle = steam_profile_cons.handler(api_key, steamid)
game_id = handle.get_game_id()


def json_builder(game_id):
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
            game_id[i]['release_date'] = release_date
            game_id[i]['recent_score'] = recent_review
            game_id[i]['total_score'] = all_review
            game_id[i]['name'] = title.replace('on Steam', '')

        except AttributeError:
            print("unable to find store page. ", i)
    print(game_id)


json_builder(game_id)

# appid = appIdList()
# here we handle the request to the specified site, and then begin to parse the data
# url ="https://store.steampowered.com/app/245370"
# html_content = requests.get(url).text
# soup = BeautifulSoup(html_content, 'lxml')

# title = soup.title.text
# recent_score = soup.find_all('in the last 30 days are positive')
# dev = soup.find_all(id="developers_list")
# describ_test = descrip.get_text()
# class_='user_reviews'
# all_score = soup.find_all()

# html = list(soup.children)
# body = list(html.children)[3]
# test = list(body.children)
# title = list(html.children)[1]
# for link in soup.find_all("a"):
#     print("Inner Text: {}".format(link.text))
#     print("Title: {}".format(link.get("title")))
#     print("class: {}".format(link.get("class")))
# print(title)

# /html/body/div[1]/div[7]/div[4]/div[1]/div[3]/div[4]/div[1]/div/div[1]/div/div[3]/div/div[1]/div[2]
