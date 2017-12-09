from setuptools import setup

setup(
    name='pycommon',
    version='1.0.0',
    packages=['pycommon', 'pycommon.patterns'],
    zip_safe=False,
    install_requires=['pymongo', 'logstash', 'python-logstash', 'diskcache']
)
