import re
import os
import csv
from copy import copy

pkg_dir, pkg_filename = os.path.split(__file__)
data_path = os.path.join(pkg_dir, "data", "countrycode_data.csv")
f = csv.reader(open(data_path, 'r'))
data = zip(*f)
data = [(x[0], x[1:]) for x in data]
data = dict(data)

def countrycode(codes=['DZA', 'CAN'], origin='iso3c', target='country_name'):
    '''Convert to and from 11 country code schemes. Use regular expressions to detect country names and standardize them. Assign region/continent descriptors.

    Parameters
    ----------

    codes : string or list of strings 
        country names or country codes to convert
    origin : string
        name of the coding scheme of origin
    target : string
        name of the coding scheme you wish to obtain

    Notes
    -----

    Valid origin codes: 
    
        * country_name 
        * iso2c : ISO 2 character
        * iso3c : ISO 3 character
        * iso3n : ISO 3 numeric
        * cown : Correlates of War numeric
        * cowc : Correlates of War character
        * un : United Nations
        * wb : World Bank
        * imf : International Monetary Fund
        * fips104 : FIPS 10-4 U.S. government geographic data
        * fao : Food & Agriculture Organization of the U.N.

    Valid target codes:

        * Any valid origin code
        * region : World Bank geographic region descriptor
        * continent : Name of continent 
    '''

    # Codes to be converted (cleanup)
    if type(codes) == str:
        codes = [codes]
        loner = True
    else:
        loner = False

    try:
        codes = ["%.0f" % x for x in codes]
    except:
        codes = [str(x).strip() for x in codes]

    # Dictionary
    target_codes = data[target]

    if origin == 'country_name':
        origin_codes = ['(?i)' + x for x in data['regex']]
    else:
        origin_codes = data[origin]

    idx = [True if (v != 'NA') and (origin_codes[i] != 'NA') else False
           for i,v in enumerate(target_codes)] 

    origin_codes = [v for i,v in enumerate(origin_codes) if idx[i]]
    target_codes = [v for i,v in enumerate(target_codes) if idx[i]]

    dictionary = dict(zip(origin_codes, target_codes))

    if origin != 'country_name':
        codes_new = ["None" if x not in origin_codes else x for x in codes]

    for k in dictionary.keys():
        codes_new = [dictionary[k] if re.match(k, x) != None else x 
                     for x in codes_new]

    # Output
    codes_new = [None if x=='None' else x for x in codes_new]

    if loner:
        codes_new = codes_new[0]

    return codes_new
