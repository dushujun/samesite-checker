#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


readme = 'README.md'
with open(readme) as f:
    long_description = f.read()


setup(
    name='samesite-checker',
    version='0.1.0',
    author='shujun.dsj',
    author_email='dushujun9@gmail.com',
    packages=find_packages(exclude=('tests', 'tests.*')),
    keywords='samesite',
    description='Samesite Checker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
)