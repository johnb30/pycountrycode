import pycountrycode
from pycountrycode import convert
from pycountrycode import data 

#TODO: input numeric codes as floats

def test_default():
    assert convert() == ['ALGERIA', 'CANADA']
def test_cown_iso3c():
    convert(origin='cown', target='iso3c', codes=['666', '315']) == ['ISR', 'nan']
def test_cn_iso3c():
    assert convert('country_name', 'iso3c', codes = ['United States', 'India', 
                   'Canada', 'Dem. Repu. Congo']) == ['USA', 'IND', 'CAN', 'COD']
def test_iso3c_cn_single():
    assert convert('iso3c', 'country_name', 'DZA') == ['ALGERIA']


