import pandas as pd
import numpy as np

def read_data(csv):
    """
    reads the csv here to avoid re-reading in the future

    Args:
        csv: the csv to be read

    Returns:
        the csv

    """
    return pd.read_csv(csv)


def get_stats(df):
    """
    Get needed stats and assign them to players.

    Args:
        df: DataFrame containing Oracle's Elixir game data.

    Returns:
        DataFrame with additional team-level stats merged for each player:
            - team_dragons: total dragons (elemental + elder) killed by team
            - team_towers: total towers destroyed by team
            - gamelength_minutes: game length in minutes
    """

    # Combine elemental and elder dragons
    df['total_dragons'] = df['dragons'].fillna(0) + df['elders'].fillna(0)

    # Group team stats per game
    team_stats = df.groupby(['gameid', 'teamname']).agg(
        team_dragons=('total_dragons', 'sum'),
        team_towers=('towers', 'sum')
    ).reset_index()

    # Merge team stats into player-level data
    df = df.merge(team_stats, on=['gameid', 'teamname'], how='left')

    # Convert game length from seconds to minutes
    df['gamelength_minutes'] = df['gamelength'] / 60

    return df

def calc_draft_kings_points(df):
    """
    Calculate Points based on these parameters:

    Player Points:
    kills                   + 3
    assists                 + 2
    death                   - 1
    cs                      - 0.02 per CS
    10 + Kills/Assists      + 2
    first_blood             + 2

    Team Points:
    team_towers             + 1
    team_dragon             + 2
    baron_kill              + 3
    result(win)             + 2
    Win < 30 min Bonus      + 2

    Args:
        df: dataframe

    Returns:
        dataframe with draft kings points

    """

    # Calculate player's individual points
    df['draft_kings_score'] = (
        df['kills'] * 3 +
        df['assists'] * 2 -
        df['deaths'] * 1 +
        df['total cs'] * 0.02 +
        df['firstbloodkill'] * 2
    )
    df['draft_kings_score'] += np.where((df['kills'] >= 10) | (df['assists'] >= 10), 2, 0)

    # Calculate team's score
    df['draft_kings_score'] = (
        df['team_towers'] * 1 +
        df['team_dragons'] * 2 +
        df['barons'] * 3
    )
    df['draft_kings_score'] += np.where(df['result'] == 1, 2, 0)
    df['draft_kings_score'] += np.where(df['gamelength_minutes'] <= 30, 2, 0)

    return df



