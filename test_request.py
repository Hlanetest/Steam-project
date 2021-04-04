import requests
from bs4 import BeautifulSoup
import steam_profile_cons

steamid = input("Enter steam ID:")
handle = steam_profile_cons.handler(steamid)

appid = get_game_id(appIdList)
#here we handle the request to the specified site, and then begin to parse the data
url ="https://store.steampowered.com/app/245370"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'lxml')

title = soup.title.text
# recent_score = soup.find_all('in the last 30 days are positive')
dev = soup.find_all(id="developers_list")
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