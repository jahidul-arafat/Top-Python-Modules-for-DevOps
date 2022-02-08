# PART-2: Create a Python CLI application with Typer Module
#2.1 Import the typer module
import typer

#2.2 Create a typer object named app
app = typer.Typer()  # Creating an typer object

#2.4 Create a simple function named hello() without any parameters
# and add a decorator so that it can be get working with the app()
# uncomment this section
# @app.command()
# def hello():
#     print("Hello")
"""
->  run the app in the terminal using
    python3 .\main.py
    python3 .\main.py hello
Note: Hence it only has one function, so by default hello() would be called without specifying the function name
"""

#2.5 What if we have multiple functions in the app().
# Add another function named goodbye() with @app.command() as decorator
@app.command()
def goodbye():
    print("Goodbye")
"""
-> Now, try to run the app in the terminal using 
python3 .\main.py                   # this will raise an error
python3 .\main.py --help            # this will list all the available options i.e. hello, goodbye
python3 .\main.py hello
python3 .\main.py goodbye
"""

# 2.6: Add two parameters: {name->string, id->integer} into the hello function
# Comment the section 2.4
# When moves to section 2.7, comment the below code
# @app.command()
# def hello(name:str, iq:int):
#     print("Hello {}".format(name))
#     print("Your IQ is: {}".format(iq))

"""
-> Now try to run the app in the terminal using
python3 .\main.py hello             # this will raise missing argument error
python3 .\main.py hello --help      # Check which arguments need to be passed and required
python3 .\main.py hello Jahid 500   # Will execute correctly
"""

# 2.7: Lets try a twist with hello() function
# Enable the user with optional disaply_iq agrument with default value: bool-> True
# If set, then the IQ value will be display
# if the user passed --no-display-iq from terminal, the IQ will be hidden

@app.command()
def hello(name: str, iq:int, display_iq:bool=True):
    print("Hello {}".format(name))
    if display_iq:
        print("Your IQ Score is: {}".format(iq))

"""
-> Now try to run the app in terminal using
python3 .\main.py hello --help                          # First check what options the helo() offers
python3 .\main.py hello Jaid 500                        # Will run as it is and display name and iq
python3 .\main.py hello Jahid 500 --no-display-iq       # Will ommit the IQ 
python3 .\main.py hello Jahid 500 --display-iq          # default is 'python3 .\main.py hello Jaid 500'
"""


#2.3 Create a python applicatin that will call the typer object named app()
if __name__ == "__main__":
    app()  # Creating a python application to call that typer object

# PART-3: Enable autocompletion in your typer module
"""
Install the typer-cli using pip3
> pip3 install typer-cli
> typer --install-completion    # this will prompt to restart the terminal. So, Restart the terminal

Now try to run the app in the terminal using
> typer .\main.py run hello Jahid 500   # typer cli has an additional parameter (run)
> typer .\main.py run h                 # press tab, this will autocomplete to `hello`

"""


