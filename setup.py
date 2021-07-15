# setup.py
from setuptools import setup, find_packages

setup(
    name='myproject',
    version='0.1',
    author="",
    author_email="",
    packages=find_packages(),
    install_requires=[
        'Click==8.0.1',
        'ruamel.yaml==0.17.10'
    ],
    entry_points='''
        [console_scripts]
        api=myproject.api:cli
    ''',
    package_data={
        "": ["*.yaml"]
    }
)
