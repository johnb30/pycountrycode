pycountrycode
-------------

Convert country names to and from 9 country code schemes.

A Python port of the ``countrycode`` package for R: 

+ `countrycode @ Github <http://github.com/vincentarelbundock/countrycode>`_
+ `countrycode @ CRAN <http://cran.r-project.org/web/packages/countrycode/index.html>`_
+ `Vincent's webpage <http://umich.edu/~varel>`_

This is *alpha* software; the script probably won't behave well in all cases. 

Dependencies
------------

+ `pandas <http://pandas.pydata.org/>`_ >= 0.9.0rc2

Installation
------------

::

    git clone https://github.com/vincentarelbundock/pycountrycode
    cd pycountrycode
    sudo python setup.py install

Usage
-----

::

    from pycountrycode import countrycode
    countrycode(origin='country_name', target='iso3c', codes=['Algeria', 'United States'])
    > ['DZA', 'USA']

