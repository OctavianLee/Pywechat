# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

url="https://github.com/OctavianLee/Pywechat"
VERSION = "0.0.1"

setup(
    name="pywechat",
    version=VERSION,
    licens='MIT',
    description="Encapsulates wechat's APIs with Python",
    author="Octavian Lee",
    author_email="octavianlee1@gmail.com",
    url = url,
    long_description="Encapsulates wechat's APIs with Python",
    install_requires=map(lambda x: x.replace('==', '>='),
        open("requirements.txt").readlines()),
    packages=find_packages(),
)
