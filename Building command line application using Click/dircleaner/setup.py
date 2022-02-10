from setuptools import setup

setup(
    name="DirectoryCleaner",        # Name of the python package
    version="1.0.2",                # Version of the 'DirectoryCleaner' python package
    py_modules=['dircleaner'],      # Module Name: dircleaner, has to be created
    install_requires=[
        'Click',                    # Setting up this python module requires a Package named 'Click'
    ],

    entry_points='''
        [console_scripts]
        dircleaner=dircleaner:cli
    ''',
)
