import os
import codecs
import frontmatter as fm
import misaka as m
from shutil import rmtree
from chevette.constants import (
    JINJA_ENV,
    OUTPUT_DIR,
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


def _get_html_filename(path):
    filename = os.path.basename(path)
    return os.path.splitext(filename)[0] + '.html'


def _render_file_to_html(metadata, content, html_filename):

    cur_dir = os.getcwd()
    public_path = os.path.join(
        cur_dir,
        OUTPUT_DIR,
        html_filename
    )
    content = m.html(content)

    with codecs.open(public_path, 'w', 'utf-8') as fd:
        layout = metadata.get('layout')
        template = JINJA_ENV.get_template(f'layouts/{layout}.html.jinja2')
        fd.write(template.render(
            content=content,
            **metadata
        ))
        fd.close()


def _render_markdown_page(file):
    html_filename = _get_html_filename(file)
    metadata, content = _parse_markdown_file(file)
    _render_file_to_html(metadata, content, html_filename)


def _parse_markdown_file(file):
    parsed_file = fm.load(file)
    return (parsed_file.metadata, parsed_file.content)


def render_template_to_file(path, new_file, _vars={}):
    # TODO: needs to be broken down into two smaller functions
    # one that renders he template
    # the other that saves the file
    with codecs.open(os.path.join(path, new_file), 'w', 'utf-8') as fd:
        template = JINJA_ENV.get_template(f'{new_file}.jinja2')
        fd.write(template.render(**_vars))
        fd.close()
