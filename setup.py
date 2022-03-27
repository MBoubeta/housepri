#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
from pathlib import Path
from setuptools import find_packages, setup

# package meta-data
NAME = 'housepri'
DESCRIPTION = "House prices prediction package."
URL = "https://github.com/MBoubeta/house-prices"
AUTHOR = "Miguel Boubeta"
# EMAIL = ""
REQUIRES_PYTHON = ">=3.6.0"

# the rest you shouldn't have to touch too much :)
# ------------------------------------------------
# except, perhaps the License and Trove Classifiers!
# if you do change the License, remember to change the
# trove classifiers for that!
long_description = DESCRIPTION

# load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR
PACKAGE_DIR = ROOT_DIR / NAME
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version


# what packages are required for this module to be executed?
def read_requirements(file="requirements.txt"):
    with open(REQUIREMENTS_DIR / file) as fd:
        return fd.read().splitlines()


# where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    # author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    package_data={"housepri": ["VERSION"]},
    install_requires=read_requirements(),
    extras_require={},
    include_package_data=True,
    license="BSD-3",
    classifiers=[
        # trove classifiers
        # full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
