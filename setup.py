from distutils.core import setup

setup(
    name='pycountrycode',
    version='0.1',
    author='Vincent Arel-Bundock',
    author_email='varel@umich.edu',
    packages=['pycountrycode'],
    #scripts=[],
    url='http://umich.edu/~varel',
    license='LICENSE.txt',
    description='Convert country names and country codes',
    long_description=open('README.rst').read(),
    package_data={'pycountrycode': ['data/countrycode_data.csv']}
)
