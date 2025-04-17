import schedule, time
from ossapi import Ossapi, Scope
from bs4 import BeautifulSoup
import requests

def create_thread():
    scope = [Scope.PUBLIC, Scope.FORUM_WRITE]
    api = Ossapi(client_id, client_secret, callback, scopes=scope)
    new_forum = api.forum_create_topic(68, "testing testing 123", "working on a bot, using this for testing")
    return new_forum.topic.id


def check_post(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    info = soup.find_all('a', class_="forum-post-info__row forum-post-info__row--username js-usercard")[-1]
    print(soup.find_all('div', class_="forum-post__content--main")[-1])
    print(info.get_text())
    print(info.get('data-user-id'))

def reply_post(id):
        scope = [Scope.PUBLIC, Scope.FORUM_WRITE]
        api = Ossapi(client_id, client_secret, callback, scopes=scope)
        new_reply = api.forum_reply(id, "just checking the functions")


def main():
    print("Hi")
    id = create_thread()
    link = "https://osu.ppy.sh/community/forums/topics/" + str(id)
    check_post(link)
    reply_post(id)
    for i in range(3):
        check_post(link)
        time.sleep(30)

if __name__ == "__main__":
    main()
    
    