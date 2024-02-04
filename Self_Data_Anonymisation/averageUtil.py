import pandas as pd

def main(df_anon, df_original, params, nb_orig_lines):
    df_anon_average = df_anon.copy()
    df_original_average = df_original.copy()
    
    # Ensure that 'average' is the second column in the DataFrames
    average_col_index = 1

    df_anon_average.iloc[:, average_col_index] = pd.to_numeric(df_anon_average.iloc[:, average_col_index], errors='coerce')
    df_original_average.iloc[:, average_col_index] = pd.to_numeric(df_original_average.iloc[:, average_col_index], errors='coerce')

    # Perform subtraction after conversion
    df_score_average = 1 - (abs(df_anon_average.iloc[:, average_col_index] - df_original_average.iloc[:, average_col_index]) / df_original_average.iloc[:, average_col_index])

    return (df_score_average.sum()) / nb_orig_lines
