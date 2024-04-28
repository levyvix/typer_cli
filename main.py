import typer
from rich import print
from rich.console import Console
from rich.table import Table
app = typer.Typer()

console = Console()

err_console =Console(stderr=True)

existing_usernames = ['admin', 'root', 'user']

@app.command()
def maybe_create_user(username: str):
    if username == 'admin':
        print('User already exists')
        raise typer.Exit(code=1)
    else:
        print('User created')

@app.command()
def print_data():
    table = Table('Name', 'Item')
    table.add_row("Rick", "Sword")
    table.add_row("Morty", "Shield")
    console.print(table)

    err_console.print('This is an error message')
@app.command()
def hello(name: str):
    """
    Say hi to NAME
    """    
    print(f'Hello {name}')


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f'Goodbye Ms. {name}. Have a good day.')
    else:
        print(f'Bye {name}!')

if __name__ == '__main__':
    app()