import tweepy
import pandas as pd

creds = pd.read_csv("/Users/Ekene/Desktop/current_proj/marvelbeings/twit_creds.csv")
# Reading tokens and secrets from a local csv instead.
con_key = creds.con_key[0]
con_sec = creds.con_sec[0]
acc_tok = creds.acc_tok[0]
acc_sec = creds.acc_sec[0]

auth = tweepy.OAuthHandler(con_key, con_sec)
auth.set_access_token(acc_tok, acc_sec)

api = tweepy.API(auth)
