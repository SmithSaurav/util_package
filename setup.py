import os

import setuptools
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="Util_Python_package",
    version="0.0.1",
    author="smith",
    author_email="smith@bdb.ai",
    description="A Util python package",
    long_description="Util Python package to use for various purposes",
    long_description_content_type="text/markdown",
    url="https://github.com/SmithSaurav/util_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: No License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)