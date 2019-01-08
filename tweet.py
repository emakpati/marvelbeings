import setup, scraper as sc, tweepy, time

api = tweepy.API(setup.auth)

i = 6

for content in sc.char_content:
    api.update_status("Today's Marvel being is " + sc.get_name(sc.char_content,i).upper() + "! #Marvel #MarvelComics #Heroes #Villains " + sc.get_url(sc.char_content,i))
    i += 1
    time.sleep(10)  # Sleep for 86400 sec (24 hours).

