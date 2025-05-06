from aggregation import *

if __name__ == "__main__":
    df = read_data("csv/2025.csv")

    # Get stats that are needed and assign to each corresponding player
    df = get_stats(df)

    # Calculate fantasy points for draft king
    df = calc_draft_kings_points(df)

    df.to_csv('output.csv', index=False)