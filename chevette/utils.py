import os
import sys
import codecs
from colorama import Fore, Style
from shutil import rmtree
from chevette.constants import ARTICLES_DIR, OUTPUT_DIR, TEMPLATES_DIR
from jinja2 import Environment, FileSystemLoader

_jinja_env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    trim_blocks=True
)


def folder_exists(path):
    return os.path.isdir(path)


def clear_directory(_dir):
    for file in os.listdir(_dir):
        file_path = os.path.join(_dir, file)

        if _is_file(file_path):
            os.unlink(file_path)
        elif _is_dir(file_path):
            rmtree(file_path)


def _is_file(path):
    return os.path.isfile(path)


def _is_dir(path):
    return os.path.isdir(path)


def print_error_and_exit(message):
    print(Fore.RED + message.strip())
    print(Style.RESET_ALL)
    sys.exit(1)


def render_template_to_file(path, new_file, _vars={}):
    with codecs.open(os.path.join(path, new_file), 'w', 'utf-8') as fd:
        template = _jinja_env.get_template(f'{new_file}.jinja2')
        fd.write(template.render(**_vars))
        fd.close()


def _generate_boilerplate(path):
    print('Generating default folder structure ...')
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    os.mkdir(os.path.join(path, ARTICLES_DIR))
    os.mkdir(os.path.join(path, OUTPUT_DIR))
    render_template_to_file(path, 'index.md')
    render_template_to_file(path, 'settings.py')
    print('Done !')
