#!/usr/bin/env python

from setuptools import setup  # , find_packages
from aiomotorengine import __version__

tests_require = [
    'nose',
    'coverage',
    'rednose',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'mongoengine',
    'docutils',
    'jinja2',
    'sphinx',
]

setup(
    name='aiomotorengine',
    version=__version__,
    description='AIOMotorEngine is an asynchronous MongoDB ORM. AIOMotorEngine uses Asyncio\'s event loop and Motor as a driver.',
    keywords='database mongodb asyncio python',
    author='Rosafi Holding',
    url='git@178.18.31.15:open/aiomotorengine.git',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4+',
    ],
    packages=['aiomotorengine'],
    include_package_data=True,
    install_requires=[
        'pymongo==2.8',
        'motor==0.5',
        'six',
        'easydict'
    ],
    use_2to3=True,
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
