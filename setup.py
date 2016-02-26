#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.1.0'

setup(
    name='whois',
    version=version,
    description='description of all the information of websites on whois lookup.',
    long_description=open('README.md').read(),
    author='Chinmay Das',
    author_email='chinmaydasbat@gmail.com',
    license='MIT',
    keywords=['whois','api', 'command line', 'cli'],
    url='https://github.com/chinmaydas96',
    packages=find_packages(),
    install_requires=[
        "requests==2.9.1"
        ,"wheel==0.29.0"

    ],
    entry_points={
        'console_scripts': [
            'whois=whois.whois:main'
        ],
    }
)