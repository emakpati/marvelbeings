import requests
from bs4 import BeautifulSoup


# url setup
url = "https://www.marvel.com/characters"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")


# Get all character cards
char_content = soup.find_all("div", class_="mvl-card mvl-card--explore")


# Get url to individual character page.
def get_url(content):
    i = 7  # First five are not characters.
    html_block = str(content[i])  # From list of divs convert into str.
    temp_path = html_block.split('url="', 1)  # Single out the url.
    path = temp_path[1].split('" data-further-details', 1)[0]
    i += 1  # Increment for next div.
    char_url = "https://www.marvel.com"+path
    return char_url

# Get name of individual character.
def get_name(content):
    i = 7
    html_block = str(content[i])
    temp_name = html_block.split('data-click-text="', 1)
    character = temp_name[1].split('" data-click-type')[0]
    i += 1
    return character









