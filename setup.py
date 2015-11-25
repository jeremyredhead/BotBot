#!/usr/bin/env python3

from setuptools import setup

setup(
    name='botbot',
    version='0.2.2',
    description='A meta-bot for Euphoria.',
    author='Rishov Sarkar',
    url='https://github.com/ArkaneMoose/BotBot',
    license='MIT',
    packages=['botbot'],
    install_requires=['eupy >=1.0, <2.0'],
    dependency_links=['git+https://github.com/jedevc/EuPy.git@7b48c35e96a1775ee37c4e5da8d3de46e99e609c#egg=eupy-1.0'],
    entry_points={
        'console_scripts': [
            'botbot = botbot.__main__:main'
        ]
    },
    test_suite='tests'
)
