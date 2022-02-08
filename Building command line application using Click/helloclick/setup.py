from setuptools import setup

setup(
    name="HelloWorld",      # Name of the python package
    version="1.0",          # Version of the 'HelloWorld' python package
    py_modules=['hello'],   # Module Name: hello, have to be created
    install_requires=[
        'Click',            # Setting up this python module requires a Package named 'Click'
    ],

    entry_points='''
        [console_scripts]
        hello=hello:cli
    ''',
)

# WhatNext ?
'''
Phase-1
-------
- [x] Create a Python Module Named 'hello': hello.py
- [x] Create a function named 'cli' in the hello.py

Phase-2
-------
- [x] Install the Python package "HelloWorld" using the following command
> cd helloclick
> pip3 install --editable .     # --editable, -e 
                                # Install a project in editable mode (i.e. setuptools “develop mode”) from a local project path or a VCS url.
                                # . --> will look for the the setup.py file for installation in the current directory
'''
