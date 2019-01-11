# -*- coding: utf-8 -*-
__author__ = 'wuwenmin1991@gmail.com'

from setuptools import setup, find_packages

with open('./README.md') as f:
    readme = f.read()

setup(
    name='dominantcolors',
    version='0.1.0',
    description='Dominant Colors',
    long_description=readme,
    author='wuwenmin',
    author_email='wuwenmin1991@gmail.com',
    py_modules=['dominantcolors'],
    packages=find_packages(include=['dominantcolors']),
    install_requires=['numpy', 'Pillow']
)
