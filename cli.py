# use click
import os
import click
from chevette import Chevette

VERSION = '1.0.0'

"""
    TODO:
        - parse command line arguments to get the project path
        - generate a settings file based on certain questions asked by the cli tool
        - generate a basic index.html template
        - turn this thing into a class
"""
@click.group()
def chevette():
    """
    Chevette is a static blog platform written in Python.
    """
    pass


@click.command()
@click.argument('path', type=str)
def new(path):
    Chevette.generate_boilerplate(path)


chevette.add_command(new)

if __name__ == "__main__":
    chevette()
