"""directory_clean_error.py: Description of what Directory Cleaning Script does."""

__author__      = "Jahidul Arafat"
__copyright__   = "Copyright 2022, JAROTBALL"
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Jahidul Arafat"
__email__ = "jahidularafat@yahoo.com"
__status__ = "Production"

import click
import os
import sys


# Some Common function
def doYouWantToContinue():
    user_response = input("Do you want to continue (Y/N)").lower()
    if user_response == "n":
        sys.exit(0)

def getFileFromDirectory(path):
    dir_content = os.listdir(path)                                                 # ['pimage8.png', 'file7.txt',...]. Only returns the file name, not the leading path of the file
    path_dir_content = [os.path.join(path,doc) for doc in dir_content]             # [./path/leading/to/your/file.txt,...]
    docs = [doc for doc in path_dir_content if os.path.isfile(doc)]                # get the list of all files, escape the folders
    folders = [folder for folder in path_dir_content if os.path.isdir(folder)]                      # return a list of all folders i.e. ['./test_directory/pn
    return (dir_content, path_dir_content, docs, folders)

def seperateFileNameFileExtension(doc):
    full_doc_path, filetype = os.path.splitext(doc)                                             # returns a tuple. os.path.splitext("./test/xyz.txt") -> ('./test/xyz', '.txt')
    doc_path = os.path.dirname(full_doc_path)                                                   # os.path.dirname("./test/xyz") -> ./test
    doc_name = os.path.basename(full_doc_path)                                                  # os.path.basename("./test/xyz") -> xyz
    return (doc_path, doc_name, filetype)

class Config(object):
    def __init__(self):
        self.verbose=False

pass_config = click.make_pass_decorator(Config, ensure=True)                                        # this will pass this 'Config' to each of the click call backs i.e. from cli() to say()
                                                                                                    # But what create this 'config' object and can you ensure that the 'config' object is really been created?
                                                                                                    # Yes, at the moment nothing created, we can set 'ensure=True' to make sure the 'config' object is created
@click.group()
@click.option('--verbose', is_flag=True,
              help="This will turn your app into verbose more")                                     # --verbose mode must not take any arguments. Thats why is_flag is set to TRUE. Default it is FALSE.
@pass_config                                                                                        # this will create a 'config' empty instance of class Config. You dont need to manually create it.
def cli(config,verbose):                                                                            # this function ever runs when a subcommand i.e. [ > hello say ] runs
    config.verbose = verbose


# Developing the <clean> operation
@cli.command()                                                                                      # subcommand of cli, instead of click as done earlier
@click.option('--path', type=click.Path(), default='.',help="Directory path of the (to be) cleaned up directory")

@pass_config                                                                                        # Ealier created 'config' instance will be passed here
def clean(config,path):
    # Add a doc string
    """This script cleans you direcotry and cluster the files accordig to their types"""

    # A first layer confirmation to make sure you accidentally dont clear any directory
    doYouWantToContinue()

    print(f"Cleaning up directory {path}")

    # Step-1: Get all files from the given directory
    dir_content, path_dir_content, docs, folders = getFileFromDirectory(path)
    moved = 0

    print(f"Cleaning up {len(docs)} of {len(dir_content)} elements")                                # i.e. Cleaning up 40 of 44 elements

    # Step-2: Rename the filepath of each file and create folder with respective file extension and move the file to the respective folder.
    # Take care of the current script which is may be running in your current path
    # Take care of the hidden_files which doesnt require to be moved
    for doc in docs:
        # 2.1 separate name from file extension
        _, doc_name, filetype = seperateFileNameFileExtension(doc)

        # 2.5 try to handle the hidden file exists, else it will raise an error
        if doc_name == "directory_clean_error" or doc_name == "test_directory_script" or doc_name.startswith("."):
            print(f"--> [{doc_name}] is either a current script or hidden file. Escaping...")
            continue

        # 2.2 get the subfolder name and create the folder if not exist
        subfolder_path = os.path.join(path, filetype[1:].lower())                                   # path-> ./text; filetype=.txt; filetype[1:]-> txt;
                                                                                                    # returns, ./text/txt and create the subfolder txt; similarly for pdf, jpg, png etc
        if subfolder_path not in folders:
            try:                                                                                    # Make sure you have try..except exceptionHandler is place
                os.mkdir(subfolder_path)                                                            # create the subfolder
                folders.append(subfolder_path)                                                      # append the folder list with the newly created subfolder
                print(f"Folder {subfolder_path} is created.")
            except FileExistsError as err:
                print(f"Folder {subfolder_path}{doc_name} already exists")                          # example; Folder /home/jarotball/Downloads/pypdf_demo-58ad283e-eb61-4767-af1f-e8b3e5e8296a already exists


        # 2.3 get the new folder path and move the file
        new_doc_path = os.path.join(subfolder_path,doc_name)+filetype                               # subfolder_path-> ./test/txt; doc_name-> file1; filetype-> .txt
                                                                                                    # returns, ./test/txt/file1.txt
        # 2.4 Now, actually move the file to their respective folder
        if new_doc_path != doc:
            os.rename(doc, new_doc_path)                                                            # os.rename("./test/file.txt", "./test/txt/file1.txt")
            print(f"Moved file {doc} to {new_doc_path}")                                            # example, Moved file ./test_directory/pfile3.pdf to ./test_directory/pdf/pfile3.pdf
            moved += 1

    print(f"Moved file {moved} of {len(docs)} files")

# Developing the <rename> operation
@cli.command()
@click.option("--search",type=str,help="To be replaced text")
@click.option("--replace",type=str,help="Text to use for replacement")
@click.option("--filetype",type=str,default=None,help="Only files with the given type will be renamed")
@click.option("--path",type=str,default=".",help="Directory path that contains the to be renamed files")

@pass_config
def rename(config, search, replace, filetype, path):
    # Add a doc string
    """
    This script rename your file in the given directory \n
    > dircleaner rename <searchText:Mandatory> <replaceText:Mandatory> --filetype <.txt|.pdf|.png> --path <path/to/your/directory>\n
    """

    # A first layer confirmation to make sure you accidentally dont clear any directory
    doYouWantToContinue()

    # little tuning
    type_filter = filetype

    print(f"Renaming files at path {path}")

    # Rename Operation begins
    # 2.1 get all files from current directory or path you passed as argument
    dir_content, path_dir_content, docs, _ = getFileFromDirectory(path)
    rename_count = 0

    print(f"{len(docs)} of {len(dir_content)} elements are files")

    # 2.2 go through all the files and check if they match the <search> pattern
    for doc in docs:
        # 2.2.1 separate the file name from file extension
        doc_path, doc_name, filetype = seperateFileNameFileExtension(doc)

        # 2.2.2 filter for files with right extension
        # Scenario-1: With filetype explicitly mentioned in cli command
        # > python3 batch_rename_cli.py <searchText:Mandatory> <replaceText:Mandatory> --filetype <.txt|.pdf|.png> --path <path/to/your/directory>

        # Scenario-2: Without filetype mentioned in cli command, in this case <type_filer is None>
        # > python3 batch_rename_cli.py <searchText:Mandatory> <replaceText:Mandatory> --path <path/to/your/directory>
        if filetype == type_filter or type_filter is None:
            # A. check if <search> text is in doc_name, then replace with <replace> text
            if search is not None and search in doc_name and replace is not None:
                # replace with given text
                new_doc_name = doc_name.replace(search, replace)
                new_doc_path = os.path.join(doc_path, new_doc_name) + filetype
                os.rename(doc, new_doc_path)                                          # Actual rename is executed here and file is successfully renamed
                rename_count += 1

                print(f"Renamed file {doc} to {new_doc_path}")

    print(f"Renamed {rename_count} of {len(docs)} files")

'''
Use Cases: clean
----------------
> dirclearner
> dirclearner --verbose
> dirclearner --help
> dirclearner clean --help
> dircleaner --verbose clean 
> dirclearner clean
> dirclearner clean --path ./test_directory
> dirclearner clean --path ~/Downloads
> dirclearner clean --path /Choose/Any/Path/You/Want/to/Clean

Use Cases: rename
--------------------
> dircleaner rename --search file --replace rfile --filetype .txt --path ./test_directory
> dircleaner rename --search file --replace rfile --path ./test_directory
'''


