import os
import codecs
from shutil import rmtree
from chevette.constants import (
    JINJA_ENV,
    EXTENSIONS_NOT_ALLOWED
)


def _is_markdown(file):
    return file.endswith('.md') or file.endswith('.markdown')


def _is_extention_allowed(file):
    file_ext = file.split('.')[1]
    return file_ext not in EXTENSIONS_NOT_ALLOWED


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


def render_template_to_file(path, new_file, _vars={}):
    # TODO: needs to be broken down into two smaller functions
    # one that renders he template
    # the other that saves the file
    with codecs.open(os.path.join(path, new_file), 'w', 'utf-8') as fd:
        template = JINJA_ENV.get_template(f'{new_file}.jinja2')
        fd.write(template.render(**_vars))
        fd.close()
