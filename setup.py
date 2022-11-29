from distutils.core import setup
from setuptools import find_packages

setup(
	name="snowflake",
	version="0.1",
	authors="Rodolfo Andrade",
	author_email="rodolfo.i.santos@fau.de",
	packages=find_packages(),
	install_requires=["numpy", "turtles"],
)