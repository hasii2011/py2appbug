
from setuptools import setup

import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

APP = ['py2appbug/py2appbug.py']

OPTIONS = {}


setup(
    name='py2appbug',
    app=APP,

    setup_requires=['py2app', 'pillow'],
    install_requires=['pillow>=11.0.0']
)
