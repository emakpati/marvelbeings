import requests
from bs4 import BeautifulSoup

url = "https://www.marvel.com/characters"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

# soup = (soup.prettify())
# Get all character cards
content = soup.find_all("div", class_="mvl-card mvl-card--explore")

def get_url(content):
    i = 6 # First five are not characters.
    html_block = str(content[i]) # From list of divs convert into str.
    temp_path = html_block.split('url="', 1) # Single out the url.
    path = temp_path[1].split(" data-further-details")[0]
    i += 1 # Increment for next div.
    url = "https://www.marvel.com"+path
    return url

print(get_url(content))

def get_name(content):
    i = 6
    html_block = str(content[i])
    temp_name = html_block.split('data-click-text="', 1)
    character = temp_name[1].split('" data-click-type')[0]
    return character

print(get_name(content))






