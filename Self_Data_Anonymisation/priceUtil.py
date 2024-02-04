import pandas as pd

def main(df_anon, df_original, params, nb_orig_lines):
    df_anon_price = df_anon.copy()
    df_original_price = df_original.copy()
    
    # Ensure that 'price' is the third column in the DataFrames
    price_col_index = 2

    # Convert 'price' columns to float, handling errors (non-numeric values) with errors='coerce'
    df_anon_price.iloc[:, price_col_index] = pd.to_numeric(df_anon_price.iloc[:, price_col_index], errors='coerce')
    df_original_price.iloc[:, price_col_index] = pd.to_numeric(df_original_price.iloc[:, price_col_index], errors='coerce')

    # Perform subtraction after conversion
    df_score_price = 1 - (abs(df_anon_price.iloc[:, price_col_index] - df_original_price.iloc[:, price_col_index]) / df_original_price.iloc[:, price_col_index])

    return (df_score_price.sum()) / nb_orig_lines

