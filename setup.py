import tweepy

con_key = "HZ2QPNKDcdfAbCLNfam8ycBmB"
con_sec = "kY6cGyyNm6tAMTdDQbUqV2axItKyLRtdWSPpsMYjdBOacxW1Mx"
acc_tok = "1065687766002855936-UfBZVgIXqA91X4RUOpgJ4YMkr1g2U9"
acc_sec = "McSM0gDOJTs0g1w3kWmhvYYwbQmnKKwMn0vOimBFYjm5U"

auth = tweepy.OAuthHandler(con_key, con_sec)
auth.set_access_token(acc_tok, acc_sec)

# get name, description, and blurb and pass into a DataFrame

