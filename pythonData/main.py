from aggregation import *

if __name__ == "__main__":
    df = read_data("csv/2025.csv")

    team_stats = df.groupby(['gameid', 'teamname']).agg(
        team_dragons=('dragons', 'sum'),
        team_firsttower=('firsttower', 'max')
    ).reset_index()

    df = df.merge(team_stats, on=['gameid', 'teamname'], how='left')