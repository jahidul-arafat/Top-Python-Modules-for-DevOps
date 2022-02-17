import sqlite3
from typing import List
import datetime
from model import Todo

conn = sqlite3.connect('todos.db')
c = conn.cursor()

# Create a function to create a table
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS todos (
        task text,
        category text,
        date_added text,
        date_completed text,
        status integer,
        position integer
    )""")

create_table()

# add()
# Create a function to insert data into table
def insert_todo(todo: Todo):
    c.execute('SELECT count(*) FROM todos')
    count = c.fetchone()[0]
    todo.position = count if count else 0
    with conn:
        c.execute('INSERT INTO todos VALUES (:task, :category, :date_added, :date_completed, :status, :position)',
                  {'task': todo.task, 'category': todo.category, 'date_added': todo.date_added, 'date_completed': todo.date_completed,
                   'status': todo.status, 'position': todo.position})

# show()
# Get the list of all todos
# -> in the function definition, These are function annotations covered in PEP 3107. Specifically, the -> marks the return function annotation.
'''
# Example 01
rd={'type':float,'units':'Joules',
    'docstring':'Given mass and velocity returns kinetic energy in Joules'}
def f()->rd:
    pass
>>> f.__annotations__['return']['type']
<class 'float'>
>>> f.__annotations__['return']['units']
'Joules'
>>> f.__annotations__['return']['docstring']
'Given mass and velocity returns kinetic energy in Joules'

# Example 02
def f(x) -> int:
    return int(x)

the -> int just tells that f() returns an integer (but it doesn't force the function to return an integer). 
It is called a return annotation, and can be accessed as f.__annotations__['return'].
'''
def get_all_todos()-> List[Todo]:
    c.execute('SELECT * FROM todos')
    results=c.fetchall()
    todos=[]
    for result in results:
        todos.append(Todo(*result)) # this will basically unpack all the arguments and place those in the constructor of our Todos class
    return todos

# delete()
# delete a todo
def delete_todo(position):
    c.execute('SELECT count(*) FROM todos')
    count = c.fetchone()[0]

    with conn:
        c.execute("DELETE from todos WHERE position=:position", {"position": position})
        for pos in range(position+1, count):
            change_position(pos,pos-1, False)   # see, here commit is False, means it will not commit at each for loop changes.
                                                # Unless, it will wait for the loop to make the changes and once done and conn closes, all changes will be automatically commited to table

def change_position(old_position:int, new_position: int, commit=True):
    c.execute("UPDATE todos SET position=:position_new WHERE position=:position_old",
              {'position_old':old_position, 'position_new':new_position})
    if commit:
        conn.commit()

# update()
# update a todo
def update_todo(position: int, task:str, category:str):
    with conn:
        if task is not None and category is not None:
            c.execute('UPDATE todos SET task=:task, category=:category WHERE position=:position',
                      {"position":position, "task":task, "category": category})
        elif task is not None:
            c.execute('UPDATE todos SET task=:task WHERE position=:position',
                      {"position":position, "task":task})
        elif category is not None:
            c.execute('UPDATE todos SET category=:category WHERE position=:position',
                      {"position":position, "category": category})

# complete()
# complete a todo
def complete_todo(position: int):
    with conn:
        c.execute('UPDATE todos SET status=2, date_completed=:date_completed WHERE position=:position',
                  {'position':position, 'date_completed':datetime.datetime.now().isoformat()})


