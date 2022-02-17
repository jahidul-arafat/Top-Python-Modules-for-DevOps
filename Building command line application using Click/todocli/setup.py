from setuptools import setup

setup(
    name="tody",                 # Name of the python package
    version="1.0.0",                # Version of the 'tody' python package
    py_modules=['todocli'],         # Module Name: todocli, has to be created
    install_requires=[
        'Click',                    # Setting up this python module requires a Package named 'Click'
        'rich',
    ],

    entry_points='''
        [console_scripts]
        tody=todocli:cli
    ''',
)
