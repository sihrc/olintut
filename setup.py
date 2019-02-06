#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='olintut',
    version='0.1',
    description='Source code for tech talk: https://docs.google.com/presentation/d/1lDDqROrpEvDYb1TcDBQBwKLQjWyTT0gs4vN1-2sraMg/edit#slide=id.g4e2f016a03_1_5',
    author='Chris Lee',
    author_email='chris@indico.io',
    packages=find_packages(),
    install_requires=open(
        os.path.join(
            os.path.dirname(__file__),
            "requirements.txt"
        ),
        'r'
    ).readlines()
)
