import click
from chevette.chevette import Chevette


@click.group()
def chevette():
    """
    Chevette is a static blog platform written in Python.
    """
    pass


@click.command()
@click.option('-f', '--force', is_flag=True, help='Force creation even if PATH already exists.')
@click.argument('path', type=str)
def new(path, force):
    """
    Generates a new chevette boilerplate at the specified PATH
    """
    Chevette.new(path, force)


@click.command()
def build():
    """
    Build your blog.
    """
    Chevette.build()


chevette.add_command(new)
chevette.add_command(build)

if __name__ == "__main__":
    chevette()
