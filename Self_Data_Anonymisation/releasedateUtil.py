import pandas as pd
import datetime as dt

def main(df_anon, df_original, params, nb_orig_lines):
    df = df_anon.copy()
    df_original_reduced = df_original.copy()

    df_score = 3 - abs(df.release_date.dt.dayofweek - df_original_reduced.release_date.dt.dayofweek)

    return (df_score.loc[df_score > 0].sum() / 3) / nb_orig_lines