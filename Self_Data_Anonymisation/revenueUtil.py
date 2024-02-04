import pandas as pd

def main(df_anon, df_original, params, nb_orig_lines):
    df_anon_revenue = df_anon.copy()
    df_original_revenue = df_original.copy()
    
    # Ensure that 'revenue' is the second column in the DataFrames
    revenue_col_index = 4

    df_anon_revenue.iloc[:, revenue_col_index] = pd.to_numeric(df_anon_revenue.iloc[:, revenue_col_index], errors='coerce')
    df_original_revenue.iloc[:, revenue_col_index] = pd.to_numeric(df_original_revenue.iloc[:, revenue_col_index], errors='coerce')

    # Perform subtraction after conversion
    df_score_revenue = 10 - (abs(df_anon_revenue.iloc[:, revenue_col_index] - df_original_revenue.iloc[:, revenue_col_index]) / df_original_revenue.iloc[:, revenue_col_index])

    return (df_score_revenue.sum()) / nb_orig_lines
