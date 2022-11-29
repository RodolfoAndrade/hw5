from distutils.core import setup
from setuptools import find_packages

setup(
	name="snowflake",
	version="0.1",
	authors="DSSS",
	author_email="luisa.e.neubig@fau.de",
	packages=find_packages(),
	install_requires=["numpy", "turtles"],
)