# Create a simple command line application named "hello" with Click module

#### 1. Create the setup.py for installation
```python
from setuptools import setup

setup(
    name="HelloWorld",      # Name of the python package
    version="1.0",          # Version of the 'HelloWorld' python package
    py_modules=['hello'],   # Module Name: hello, have to be created
    install_requires=[
        'Click',            # Setting up this python module requires a Package named 'Click'
    ],

    entry_points='''
        [console_scripts]   # Means this will execute in the console i.e. > hello --help 
                            #                                             > hello
                            #                                             > hello --verbose etc
        hello=hello:cli     #console_cmd_name=pythonModuleName:Method_to_be_called
                            #console_cmd_name       = hello
                            +pythonModuleName       = hello
                            +Method_to_be_called    =cli
    ''',
)
```
# WhatNext ?
```python
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
'''
```
