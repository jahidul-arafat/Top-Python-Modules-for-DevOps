"""todocli.py: Description of what Todocli does."""

__author__ = "Jahidul Arafat"
__copyright__ = "Copyright 2022, JAROTBALL"
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Jahidul Arafat"
__email__ = "jahidularafat@yahoo.com"
__status__ = "Production"

import click
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, insert_todo, delete_todo, update_todo, complete_todo

console = Console()

# Common function
# list_all_todos()
def list_all_todos():
    """List all tasks"""
    tasks = get_all_todos()

    console.print("[bold magenta]Todos[/bold magenta]!", "💻")

    # create the table
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        CAT_COLOR_DICT = {
            "Learn": "cyan",
            "Youtube": "red",
            "Sports": "cyan",
            "Study": "green"
        }

        if category in CAT_COLOR_DICT.keys():
            return CAT_COLOR_DICT[category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)  # task[0]->todo, task[1]-> category
        is_done_str = '✅' if task.status == 2 else '❌'
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)

    console.print(table)

# Develop the cli and cli.command().
# Without click.group(), cli.command() will not work
@click.group()
def cli():  # this function ever runs when a subcommand i.e. [ > hello say ] runs
    pass


# 5x Core Components
'''
- add(task, category)
- delete(position)
- update(position, task, category)
- complete(position)
- show()
'''


# add()
# 2x params: task and category
# usage: python3 todocli.py add "Add Your Task Here" "Set Category Name"
@cli.command()
@click.option("--task",'-t', type=str, help="Task to be added")
@click.option("--category",'-c', type=str, help="Category of the task")
def add(task, category):
    """Add an item"""
    click.echo(f"adding {task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)
    list_all_todos()


# delete
# 1x params: position of task
# usage: python3 todocli.py delete 3
@cli.command()
@click.option("--position",'-i', type=int, help="Enter the Task No to delete")
def delete(position):
    """Delete a task"""
    click.echo(f"deleting {position}")
    # Indices in Console starts at 1, but at database it starts at 0
    delete_todo(position - 1)
    list_all_todos()


# update()
# 3x params: position, task=None, category=None
# Usage: python3 todocli.py update 6 --task "Updated Task name"
@cli.command()
@click.option("--position",'-i', type=int, help="Enter the Task No to be updated")
@click.option("--task",'-t', type=str, default=None, help="Task to be added")
@click.option("--category",'-c', type=str, default=None, help="Category of the task")
def update(position, task, category):
    """Update a task"""
    click.echo(f"updating {position}")
    update_todo(position - 1, task, category)
    list_all_todos()


# complete()
# 1x params: position
# Usage: python3 todocli.py complete 3
@cli.command()
@click.option("--position",'-i', type=int, help="Mark the Task No as completed")
def complete(position):
    """Mark the task completed"""
    click.echo(f"complete {position}")
    complete_todo(position - 1)
    list_all_todos()


# show() - list all tasks with category
# Usage: python3 todolci.py show
@cli.command()
def show():
    list_all_todos()
