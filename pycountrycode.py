import pandas as pd
import re

# Conversion table
data = pd.read_csv('countrycode_data.csv')

# Conversion function
def convert(origin='iso3c', target='country_name', codes=['DZA', 'CAN']):
    # Codes to clean strings
    if type(codes) == str:
        codes = [codes]
    target_codes = map(lambda x: re.sub('.0', '', str(x).strip()), data[target])
    if origin == 'country_name':
        origin_codes = map(lambda x: re.sub('.0', '', str(x).strip()), data['regex'])
    else:
        origin_codes = map(lambda x: re.sub('.0', '', str(x).strip()), data[origin])
    # Conversion dictionary
    dictionary = dict(zip(origin_codes, target_codes))
    dictionary['nan'] = 'nan'
    # For each origin code in dict, map substitution to input code list
    if origin != 'country_name':
        for val in dictionary:
            old = '^' + str(val) + '$'
            new = dictionary[val]
            codes = map(lambda x: re.sub(old, new, x), codes)
    else:
        for idx, val in enumerate(dictionary):
            old = '(?i)' + val 
            new = dictionary.values()[idx]
            codes = map(lambda x: re.sub(old, new, x), codes)
    return codes


