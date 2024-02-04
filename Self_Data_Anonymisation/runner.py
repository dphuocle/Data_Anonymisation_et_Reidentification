import dateUtil
import distanceUtil
import priceUtil
import sqft_livingUtil

import pandas as pd
import subprocess
import argparse

def open_dataframe(arg):
    file = open(arg)
    df = pd.read_csv(file, delimiter='\t', header=None, 
        dtype={'price': 'category', 'sqft_living': 'category', 'lat': 'category', 'long': 'category'},
        names=['id', 'date', 'price', 'sqft_living', 'lat', 'long'])
    # Change types
    df['date'] = pd.to_datetime(df['date'])
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("anonymized", help="Anonymized Dataframe filename")
    parser.add_argument("original", help="Original Dataframe filename")
    parser.add_argument("script", help="Script to use for testing",
        choices=['dateUtil', 'distanceUtil', 'priceUtil', 'sqft_livingUtil'] )
    args = parser.parse_args()

    df_origin = open_dataframe(args.original)
    df_anon = open_dataframe(args.anonymized)
    size_df = len(df_origin)

    score = 0

    if args.script == "dateUtil":
        score = dateUtil.main(df_anon, df_origin, {}, size_df)
    elif args.script == "distanceUtil":
        score = distanceUtil.main(df_anon, df_origin, {"dx_distance":1}, size_df)
    elif args.script == "priceUtil":
        score = priceUtil.main(df_anon, df_origin, {}, size_df)
    elif args.script == "sqft_livingUtil":
        score = sqft_livingUtil.main(df_anon, df_origin, {}, size_df)
    else:
        print("No script run. Exiting...")
        exit()

    print(score)