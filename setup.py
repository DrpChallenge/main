#!/usr/bin/env python
from distutils.core import setup

from setuptools import find_packages

setup(name='drp',
      version='0.1',
      python_requires=">=3.8",
      packages=find_packages(),
      package_data={
          "drp_env": ["config/*.yaml", "map/*/*.csv"],
          }
    )