import tweepy, setup, scraper as sc, time

api = tweepy.API(setup.auth)

api.update_status("Today's Marvel being of the day is "+sc.get_name(sc.content).upper()+"!"+sc.get_url(sc.content))