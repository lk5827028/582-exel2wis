# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='excel2wisxml',
    version='1.0.0',
    include_package_data = True,
    packages=["excel2wisxml"],
    install_requires=[
        'xlrd',
        'lxml',
        'argparse',
    ],
    zip_safe = False,
    entry_points={
        'console_scripts': [
            'excel2wisxml = excel2wisxml.excel2wisxml:main']
    }
)
