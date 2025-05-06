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

def calc_draft_kings_points(df):
    """
    Calculate Points based on these parameters:

    kills                   + 3
    assists                 + 2
    death                   - 1
    cs                      - 0.02 per CS
    first_blood             + 2
    first_turrent           + 1
    dragon_kill             + 0.3 points per drag kill divided by number of players(5)
    first_dragon
    baron_kill              + 2
    result(win)             + 2

    ** Noted additional points **
    10 + Kills/Assists      + 2
    Win < 30 min Bonus      + 2

    Args:
        df: dataframe

    Returns:
        dataframe with draft kings points

    """

    df['draft_kings_score'] = (
        df['kills'] * 3 +
        df['assists'] * 2 -
        df['deaths'] * 1 +
        df['total cs'] * 0.02 +
        df['firstbloodkill'] * 2 +
        df['firsttower'] * 2 +
        (df['dragons'] * 0.3) / 5
    )

    df['draft_kings_score'] += np.where(df['kills'] >= 10, 2, 0)



