import setup, scraper as sc, tweepy, time


i = 6  # To be passed to get_name() and get_url() from scraper.py.

for content in sc.char_content:
    setup.api.update_status(f"Today's Marvel character is {sc.get_name(sc.char_content,i).upper()}" +
                      f" 🤖 #Marvel #MarvelComics #Heroes #Villains {sc.get_url(sc.char_content,i)}")
    i += 1
    print("Posting character " + str(i) + ".")
    time.sleep(86400)  # Sleep for 86400 (24 hrs).


