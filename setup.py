from setuptools import setup, find_packages

setup(
    name='PyBnB',
    version='0.1',
    packages=find_packages(),
    install_requires=['firebase-admin','pandas','selenium',],
)