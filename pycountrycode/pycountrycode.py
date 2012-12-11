import pandas as pd
import re
import pkgutil
import StringIO

# Conversion table
csvdata = pkgutil.get_data(__name__, 'data/countrycode_data.csv')
csvio = StringIO.StringIO(csvdata)
data = pd.read_csv(csvio)

# Conversion function
def countrycode(origin='iso3c', target='country_name', codes=['DZA', 'CAN'], data=data):
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


