from setuptools import setup, find_packages
from pkg_resources import parse_requirements

with open("requirements.txt") as f:
    REQUIREMENTS = [str(req) for req in parse_requirements(f.read())]

setup(
    name='AVR testing scripts',
    version='0.1.0',
    description='Testing scripts',
    author='Bogumil Zebek',
    author_email='',
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    install_requires=REQUIREMENTS
)