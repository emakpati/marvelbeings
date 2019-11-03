import requests
from bs4 import BeautifulSoup

# url setup
url = "https://www.marvel.com/characters"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

tweeted_chars = []

# Get all character cards
char_content = soup.find_all("div", class_="mvl-card mvl-card--explore")
print(type(char_content),"\n", char_content)


# Get url to individual character page.
def get_url(content, i):
    # First five are not characters.
    html_block = str(content[i])  # From list of divs convert into str.
    temp_path = html_block.split('url="', 1)  # Single out the url.
    path = temp_path[1].split('" data-further-details', 1)[0]
    char_url = "https://www.marvel.com"+path
    return char_url


# Get name of individual character.
def get_name(content, i):
    html_block = str(content[i])
    temp_name = html_block.split('data-click-text="', 1)
    character = temp_name[1].split('" data-click-type')[0]
    tweeted_chars.append(character)
    return character








