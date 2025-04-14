from ossapi import Ossapi, Scope
from bs4 import BeautifulSoup
import requests
import time

client_id = *
client_secret = "*"
callback_url = "*"
scopes = [Scope.PUBLIC, Scope.FORUM_WRITE]
api = Ossapi(client_id, client_secret, callback_url, scopes=scopes)
forum = api.forum_topic(2058165)
print(forum)
# soup = BeautifulSoup(forum, 'html.parser')

# info = soup.find_all('a', class_="forum-post-info__row forum-post-info__row--username js-usercard")[-1]
# print(info.get_text())
# print(info.get('data-user-id'))