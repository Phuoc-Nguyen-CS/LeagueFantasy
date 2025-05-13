from aggregation import *
import pandas as pd

pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


if __name__ == "__main__":
    df = read_data("csv/2025.csv")
    df = regions(df)
    df.drop("url", axis=1, inplace=True)

    # Assign only the columns needed to make the calculations to reduce clutter
    fp_df = needed_columns(df)
    # Get stats that are needed and assign to each corresponding player
    fp_df = get_stats(fp_df)

    # Calculate fantasy points for draft king
    fp_df = calc_draft_kings_points(fp_df)
    fp_df = fp_df[fp_df['position'] != 'team'].copy()

    print(fp_df.sort_values('draft_kings_score', ascending=False))
    fp_df.to_csv('output.csv', index=False)
