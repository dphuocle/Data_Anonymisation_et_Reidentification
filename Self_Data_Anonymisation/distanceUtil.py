def calcul_utility_distance(diff_distance):
    score_distance = diff_distance*(-1/dx_distance) + 1
    if(score_distance < 0):
        return 0
    return score_distance

def main(df_anon, df_original, params, nb_orig_lines):
    global dx_distance
    dx_distance = params['dx_distance']

    df_anon_distance = df_anon.copy()
    df_original_distance = df_original.copy()

    # Converting longitude and latitude as float 
    df_anon_distance = df_anon_distance.astype({'price': 'float64', 'sqft_living': 'float64', 'lat': 'float64', 'long': 'float64'})
    df_original_distance = df_original_distance.astype({'price': 'float64', 'sqft_living': 'float64', 'lat': 'float64', 'long': 'float64'})
    
    df_anon_distance['lat'] = abs(df_anon_distance['lat'] - df_original_distance['lat'])
    df_anon_distance['long'] = abs(df_anon_distance['long'] - df_original_distance['long'])
    df_anon_distance['diff_distance'] = df_anon_distance['lat'] + df_anon_distance['long']
    df_anon_distance['score_distance'] = df_anon_distance['diff_distance'].apply(calcul_utility_distance)
    score = df_anon_distance['score_distance'].sum()
    return score / nb_orig_lines