from ossapi import Ossapi, Scope
from bs4 import BeautifulSoup
import requests

scope = [Scope.PUBLIC, Scope.FORUM_WRITE]
api = Ossapi(client_id, client_secret, callback, scopes=scope)
new_forum = api.forum_create_topic(68, "testing testing 123", "working on a bot, using this for testing")
id = new_forum.topic.id
link = "https://osu.ppy.sh/community/forums/topics/" + str(id)
new_reply = api.forum_reply(id, "just checking the functions")
page = requests.get(link)
soup = BeautifulSoup(page.text, 'html.parser')
info = soup.find_all('a', class_="forum-post-info__row forum-post-info__row--username js-usercard")[-1]
print(info.get_text())
print(info.get('data-user-id'))



