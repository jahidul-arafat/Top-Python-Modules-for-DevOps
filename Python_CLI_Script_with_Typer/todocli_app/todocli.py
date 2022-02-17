#!/usr/bin/env python3
#sqlite3 tutorial: https://www.sqlitetutorial.net/sqlite-commands/

import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, insert_todo, delete_todo, update_todo, complete_todo

console = Console()


# Create a typer object named "app"
app = typer.Typer()

# add()
# 2x params: task and category
# usage: python3 todocli.py add "Add Your Task Here" "Set Category Name"
@app.command(short_help='adds an item')
def add(task:str, category:str):
    typer.echo(f"adding {task}, {category}")
    todo=Todo(task,category)
    insert_todo(todo)
    show()

# delete
# 1x params: position of task
# usage: python3 todocli.py delete 3
@app.command(short_help="Delete a task")
def delete(position: int):
    typer.echo(f"deleting {position}")
    # Indices in Console starts at 1, but at database it starts at 0
    delete_todo(position-1)
    show()

# update()
# 3x params: position, task=None, category=None
# Usage: python3 todocli.py update 6 --task "Updated Task name"
@app.command(short_help="Update a task")
def update(position:int, task: str=None, category: str=None):
    typer.echo(f"updating {position}")
    update_todo(position-1,task,category)
    show()

# complete()
# 1x params: position
# Usage: python3 todocli.py complete 3
@app.command(short_help="Mask the task completed")
def complete(position:int):
    typer.echo(f"complete {position}")
    complete_todo(position-1)
    show()

# show() - list all tasks with category
# Usage: python3 todolci.py show
@app.command(short_help="List all tasks")
def show():
    # tasks = [
    #     ("Todo1", "Study"),
    #     ("Todo2","Sports")
    # ]
    tasks = get_all_todos()

    console.print("[bold magenta]Todos[/bold magenta]!", "💻")

    # create the table
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        CAT_COLOR_DICT ={
            "Learn":"cyan",
            "Youtube":"red",
            "Sports":"cyan",
            "Study":"green"
        }

        if category in CAT_COLOR_DICT.keys():
            return CAT_COLOR_DICT[category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)         # task[0]->todo, task[1]-> category
        is_done_str = '✅' if task.status == 2 else '❌'
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)

    console.print(table)


if __name__ == "__main__":
    app()  # Creating a python application to call that typer object
