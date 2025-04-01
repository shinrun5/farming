from bs4 import BeautifulSoup
import requests
#inlcude <string>

url = "https://osu.ppy.sh/community/forums/topics/2047212?n=1cl"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
"""print(soup.get_text()) //get all text
print(soup.find(class_="bbcode"))"""

info = soup.find_all('a', class_="forum-post-info__row forum-post-info__row--username js-usercard")[-1]
print(info.get_text())
print(info.get('data-user-id'))


#results = soup.find_all('div', class_="bbcode")[-1]
#for row in results:
#    print(row)




#print(results)