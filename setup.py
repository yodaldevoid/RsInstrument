"""Setup file for creating the RsInstrument package."""

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()

# This call to setup() does all the work
setup(
	name="RsInstrument",
	version="1.53.0",
	description="VISA or Socket Communication Module for Rohde & Schwarz Instruments",
	long_description=README,
	long_description_content_type="text/x-rst",
	author="Rohde & Schwarz GmbH & Co. KG",
	copyright="Copyright © Rohde & Schwarz GmbH & Co. KG 2022",
	url="https://github.com/Rohde-Schwarz/RsInstrument",
	license="MIT",
    classifiers=['License :: OSI Approved :: MIT License',
                 'Intended Audience :: Developers',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX :: Linux',
                 'Operating System :: MacOS :: MacOS X',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'Programming Language :: Python :: 3.10'
                ],
	packages=(find_packages(include=['RsInstrument', 'RsInstrument.*'])),
    install_requires=['PyVisa>=1.11.3'],
    python_requires='>=3.6'
)
