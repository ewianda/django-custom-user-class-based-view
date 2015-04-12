from setuptools import setup, find_packages
import os
setup( 
    install_requires=[
        'setuptools',
        'Django>=1.5',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False)
