import releasedateUtil
import averageUtil
import countUtil
import revenueUtil

import pandas as pd
import subprocess
import argparse

def open_dataframe(arg):
    file = open(arg)
    df = pd.read_csv(file, delimiter='\t', header=None, 
        dtype={'id': 'category', 'vote_average': 'category', 'vote_count': 'category', 'revenue': 'category'},
        names=['id', 'vote_average', 'vote_count', 'release_date', 'revenue'])
    # Change types
    df['release_date'] = pd.to_datetime(df['release_date'])
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("anonymized", help="Anonymized Dataframe filename")
    parser.add_argument("original", help="Original Dataframe filename")
    parser.add_argument("script", help="Script to use for testing",
        choices=['releasedateUtil', 'averageUtil', 'countUtil', 'revenueUtil'] )
    args = parser.parse_args()

    df_origin = open_dataframe(args.original)
    df_anon = open_dataframe(args.anonymized)
    size_df = len(df_origin)

    score = 0

    if args.script == "releasedateUtil":
        score = releasedateUtil.main(df_anon, df_origin, {}, size_df)
    elif args.script == "averageUtil":
        score = averageUtil.main(df_anon, df_origin, {}, size_df)
    elif args.script == "countUtil":
        score = countUtil.main(df_anon, df_origin, {}, size_df)
    elif args.script == "revenueUtil":
        score = revenueUtil.main(df_anon, df_origin, {}, size_df)
    else:
        print("No script run. Exiting...")
        exit()

    print(score)