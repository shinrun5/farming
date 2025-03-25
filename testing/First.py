from bs4 import BeautifulSoup
import requests
url = "https://osu.ppy.sh/community/forums/topics/2047212?n=1cl"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)