from setuptools import setup, find_packages
from os import path

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='pyciderevalcap',
    version='1.0.0',
    description='pyciderevalcap',
    packages=find_packages(),
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    zip_safe=False,
    install_requires=requirements,
)
