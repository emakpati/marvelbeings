import tweepy

con_key = "cGwJSXhV3wtfpHqjdA8o6CbxN"
con_sec = "Hv3NGPWRQxF6anxOtLzHpj4GB1Vc3I1twlgTB9FsumflvKjBvm "
acc_tok = "1065687766002855936-UFjq9dsOMWXXIIcc1xXj4Tx1c2TfST"
acc_sec = "gqQI0DMORV6gCrxilVQNQgt1N3V763xO75MuZWsooWkgF"

auth = tweepy.OAuthHandler(con_key, con_sec)
auth.set_access_token(acc_tok, acc_sec)
api = tweepy.API(auth)

# get name, description, and blurb and pass into a DataFrame

