from pycountrycode import countrycode

def test_default():
    assert countrycode() == ['ALGERIA', 'CANADA']

def test_cown_iso3c():
    assert countrycode(codes=['666', '315'], origin='cown', target='iso3c') == ['ISR', 'BHS']

def test_cn_iso3c():
    assert countrycode(['United States', 'India', 'Canada', 'Dem. Repu. Congo'], 
            'country_name', 'iso3c') == ['USA', 'IND', 'CAN', 'COD']

def test_iso3c_cn_single():
    assert countrycode('DZA', 'iso3c', 'country_name') == 'ALGERIA'
