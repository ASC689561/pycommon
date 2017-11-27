from setuptools import setup, find_packages

setup(
    name='pycommon',
    version='1.0.0',
    # packages=find_packages(exclude=('tests', 'common.egg-info'),include=['*.py','processor/*.py']),
    packages=['pycommon','pycommon.patterns'],
    zip_safe=False,
    install_requires=['pymongo', 'logstash', 'python-logstash','diskcache']
)
