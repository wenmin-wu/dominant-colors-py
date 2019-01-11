# -*- coding: utf-8 -*-
__author__ = 'wuwenmin1991@gmail.com'

from setuptools import setup, find_packages

with open('./README.md') as f:
    readme = f.read()

setup(
    name='dominantcolors',
    version='0.1.0',
    description='A module to grab dominant colors from image',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/wenmin-wu/dominant-colors-py",
    author='wuwenmin',
    author_email='wuwenmin1991@gmail.com',
    py_modules=['dominantcolors'],
    install_requires=['numpy', 'Pillow']
)
