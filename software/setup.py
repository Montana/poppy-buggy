#!/usr/bin/env python

import re
import sys
from setuptools import setup, find_packages

def get_version():
    with open('poppy_buggy/_version.py') as file:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", file.read(), re.MULTILINE).group(1)

def get_extra_options():
    extra = {}
    if sys.version_info >= (3,):
        extra['use_2to3'] = True
    return extra

setup(
    name='poppy-buggy',
    version=get_version(),
    packages=find_packages(),
    install_requires=['pypot >= 3', 'hampy'],
    include_package_data=True,
    exclude_package_data={'': ['README', '.gitignore']},
    zip_safe=False,
    author='https://github.com/poppy-project/poppy-buggy/graphs/contributors',
    author_email='brice.copy@cern.ch',
    description='Poppy Buggy Software Library',
    url='https://github.com/CERN/poppy-buggy',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    **get_extra_options()
)
