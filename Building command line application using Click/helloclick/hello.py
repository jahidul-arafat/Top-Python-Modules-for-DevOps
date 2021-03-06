import click

# Scenario-01: Using Cli function and No Click.group() to create a cmd line application
# @click.command()
# @click.option('--string', default="World",
#               help="This is the named that is greeted")
# @click.option('--repeat', default=1,
#               help="How many times to greet")
# @click.argument('out', type=click.File('w'),
#                 default='-', required=False)                    # mendatory argument, comes after all the options
#                                                                 # type=int/str or click type. click type is more powerful
#                                                                 # Convert this mendatory argument optional using defualt and required parameter
# def cli(string,repeat,out):
#     # Add a doc string
#     """This script greets you"""
#     #click.echo(out)
#     for x in range(repeat):
#         click.echo(f"Attempt: {x+1} Hello {string}",file=out)   # this file is LAZY by default.
#                                                                 # Means, unless you write something in this file, it doesn't open

# Scenario-02: Using click.group() to modify the above command line application
# Any click.group can have subcommands
# Following chanages we would made
'''
- [x] Change the cli() method to say() method
- [x] using click.group() and create a new cli function
- [x] modify the earlier click.command() to cli.command() ,  
'''

# Answer of Question-01
# Create a COnfig class with an empty constructor
# class Config(object):
#     def __init__(self):
#         self.verbose=False
#
# pass_config = click.make_pass_decorator(Config, ensure=True)    # this will pass this 'Config' to each of the click call backs i.e. from cli() to say()
#                                                                 # But what create this 'config' object and can you ensure that the 'config' object is really been created?
#                                                                 # Yes, at the moment nothing created, we can set 'ensure=True' to make sure the 'config' object is created
# @click.group()
# @click.option('--verbose', is_flag=True)                        # --verbose mode must not take any arguments. Thats why is_flag is set to TRUE. Default it is FALSE.
# @pass_config                                                    # this will create a 'config' empty instance of class Config. You dont need to manually create it.
# def cli(config,verbose):                                        # this function ever runs when a subcommand i.e. [ > hello say ] runs
#     config.verbose = verbose
#     # if verbose:
#     #     click.echo("We are in Verbose Mode")
#
# @cli.command()                                                  # subcommand of cli, instead of click as done earlier
# @click.option('--string', default="World",
#               help="This is the named that is greeted")
# @click.option('--repeat', default=1,
#               help="How many times to greet")
# @click.argument('out', type=click.File('w'),
#                 default='-', required=False)                    # mendatory argument, comes after all the options
#                                                                 # type=int/str or click type. click type is more powerful
#                                                                 # Convert this mendatory argument optional using defualt and required parameter
# @pass_config                                                    # Ealier created 'config' instance will be passed here
# def say(config,string,repeat,out):
#     # Add a doc string
#     """This script greets you"""
#     #click.echo(out)
#     if config.verbose:
#         click.echo("We are in Verbose Mode!!!")
#     for x in range(repeat):
#         click.echo(f"Attempt: {x+1} Hello {string}",file=out)   # this file is LAZY by default.

'''
Question-01: When you run, we get the following output
> hello --verbose say
---
We are in Verbose Mode
Attempt: 1 Hello World
---
But, how the cli() function is communicating the say() function?
Simulate this with a config object. [See Above ^^^^^]
'''

# Scenario 03: Let the parent cmd i.e. 'hello' takes an argument called '--home-dir' and pass it to its subcommand 'say',
# which will print the path of the '--home-dir'
class Config(object):
    def __init__(self):
        self.verbose=False

pass_config = click.make_pass_decorator(Config, ensure=True)    # this will pass this 'Config' to each of the click call backs i.e. from cli() to say()
                                                                # But what create this 'config' object and can you ensure that the 'config' object is really been created?
                                                                # Yes, at the moment nothing created, we can set 'ensure=True' to make sure the 'config' object is created
@click.group()
@click.option('--verbose', is_flag=True,
              help="This will turn your app into verbose more") # --verbose mode must not take any arguments. Thats why is_flag is set to TRUE. Default it is FALSE.
@click.option('--home-directory', type=click.Path(), default='.',
              help="Set the home directory of you app, default is current directory")
@pass_config                                                    # this will create a 'config' empty instance of class Config. You dont need to manually create it.
def cli(config,verbose,home_directory):                         # this function ever runs when a subcommand i.e. [ > hello say ] runs
    config.verbose = verbose
    config.home_directory = home_directory
    # if verbose:
    #     click.echo("We are in Verbose Mode")

@cli.command()                                                  # subcommand of cli, instead of click as done earlier
@click.option('--string', default="World",
              help="This is the named that is greeted")
@click.option('--repeat', default=1,
              help="How many times to greet")
@click.argument('out', type=click.File('w'),
                default='-', required=False)                    # mendatory argument, comes after all the options
                                                                # type=int/str or click type. click type is more powerful
                                                                # Convert this mendatory argument optional using defualt and required parameter
@pass_config                                                    # Ealier created 'config' instance will be passed here
def say(config,string,repeat,out):
    # Add a doc string
    """This script greets you"""
    #click.echo(out)
    if config.verbose:
        click.echo("We are in Verbose Mode!!!")

    # printing the home_directory passed from the parent function i.e. cli() to say()
    click.echo(f"Home Directory: {config.home_directory}")

    for x in range(repeat):
        click.echo(f"Attempt: {x+1} Hello {string}",file=out)   # this file is LAZY by default.

