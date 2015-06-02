# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

url="https://github.com/OctavianLee/Pywechat"
VERSION = "0.0.2"

setup(
    name="pywechat",
    version=VERSION,
    license='MIT',
    description="A python SDK for the wechat public platform.",
    author="Octavian Lee",
    author_email="octavianlee1@gmail.com",
    url = url,
    long_description="A python SDK for the wechat public platform.",
    install_requires=map(lambda x: x.replace('==', '>='),
        open("requirements.txt").readlines()),
    packages=find_packages(),
)
