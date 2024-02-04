import pandas as pd

def main(df_anon, df_original, params, nb_orig_lines):
    df_anon_sqft = df_anon.copy()
    df_original_sqft = df_original.copy()
    
    # Ensure that 'sqft_living' is the fourth column in the DataFrames
    sqft_col_index = 3

    # Convert 'sqft_living' columns to float, handling errors (non-numeric values) with errors='coerce'
    df_anon_sqft.iloc[:, sqft_col_index] = pd.to_numeric(df_anon_sqft.iloc[:, sqft_col_index], errors='coerce')
    df_original_sqft.iloc[:, sqft_col_index] = pd.to_numeric(df_original_sqft.iloc[:, sqft_col_index], errors='coerce')

    # Perform subtraction after conversion
    df_score_sqft = 1 - (abs(df_anon_sqft.iloc[:, sqft_col_index] - df_original_sqft.iloc[:, sqft_col_index]) / df_original_sqft.iloc[:, sqft_col_index])

    return ((df_score_sqft.sum()) / nb_orig_lines)

