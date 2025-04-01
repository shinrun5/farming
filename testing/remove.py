from bs4 import BeautifulSoup
import requests
#inlcude <string>

url = "https://osu.ppy.sh/community/forums/topics/2047212?n=1cl"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
"""print(soup.get_text()) //get all text
print(soup.find(class_="bbcode"))"""

results = soup.find_all('div', class_="bbcode")



print(results)