import multiprocessing
from setuptools import setup, find_packages

test_requirements = ['sentinels>=0.0.6', 'nose>=1.0', 'python-dateutil>=2.2', 'pytest>=2.7.2']

setup(
    name = "redis-py-threaded",
    version = "0.0.1",
    packages = find_packages(),

    # Dependencies on other packages:
    setup_requires   = ['nose>=1.1.2'],
    tests_require    = test_requirements,
    install_requires = [
			'hiredis>=0.2.0',
			] + test_requirements,

    # Unit tests; they are initiated via 'python setup.py test'
    test_suite       = 'nose.collector', 

    #data_files = [('pymysql_utils/data', datafiles)],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
     #   '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
     #   'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "Andreas Paepcke",
    author_email = "paepcke@cs.stanford.edu",
    description = "Provides a software bus type API over Redis.",
    license = "BSD",
    keywords = "Redis, OpenEdX",
    url = "https://github.com/paepcke/redis-py-threaded",   # project home page, if any
)
