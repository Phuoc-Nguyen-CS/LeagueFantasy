import pandas as pd

# Points:
# Kills + 3
# Assists + 2
# Deaths - 1
# Creep Score + 0.02
# 10+ K/A Bonus + 2

# We need to calculate their average amount of points earned per game
# Can do Season and past Seasons

def getPlayerName(csv):
    df = pd.read_csv(csv)
    headers = list(df.columns)
    print(headers)

