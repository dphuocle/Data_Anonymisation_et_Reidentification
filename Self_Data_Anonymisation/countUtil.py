import pandas as pd

def main(df_anon, df_original, params, nb_orig_lines):
    df_anon_count = df_anon.copy()
    df_original_count = df_original.copy()
    
    # Ensure that 'count' is the second column in the DataFrames
    count_col_index = 2

    df_anon_count.iloc[:, count_col_index] = pd.to_numeric(df_anon_count.iloc[:, count_col_index], errors='coerce')
    df_original_count.iloc[:, count_col_index] = pd.to_numeric(df_original_count.iloc[:, count_col_index], errors='coerce')

    # Perform subtraction after conversion
    df_score_count = 6 - (abs(df_anon_count.iloc[:, count_col_index] - df_original_count.iloc[:, count_col_index]) / df_original_count.iloc[:, count_col_index])

    return (df_score_count.sum()) / nb_orig_lines
