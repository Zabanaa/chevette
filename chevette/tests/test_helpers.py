import pytest
from chevette.utils.helpers import (
    _is_markdown,
    _is_extention_allowed,
    _get_html_filename,
    _print_error_and_exit,
    folder_exists,
    clear_directory,
    _is_file,
)
from chevette.utils.constants import EXTENSIONS_NOT_ALLOWED


def escape_ansi(line):
    import re
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line)


def test_is_markdown():
    assert _is_markdown('hello.md') == True
    assert _is_markdown('hello.markdown') == True
    assert _is_markdown('pipfile') == False


def test_is_extension_allowed():
    assert _is_extention_allowed('some_file_without_extension') == False
    assert _is_extention_allowed('index.html') == True
    for ext in EXTENSIONS_NOT_ALLOWED:
        filename = 'test.' + ext
        assert _is_extention_allowed(filename) == False


def test_get_html_filename():
    filename = 'file'
    html_filename = _get_html_filename(f'/path/to/some/{filename}.ext')
    html_filename_no_ext = _get_html_filename(f'/path/to/some/{filename}')
    html_filename_relative_path = _get_html_filename(f'{filename}.ext')
    assert html_filename == filename + '.html'
    assert html_filename_no_ext == filename + '.html'
    assert html_filename_relative_path == filename + '.html'


def test_print_error_and_exit(capsys):
    error_message = 'Some error message'
    with pytest.raises(SystemExit):
        _print_error_and_exit(error_message)
    captured = capsys.readouterr()
    escaped_output = escape_ansi(captured.out)
    assert escaped_output.rstrip() == error_message


def test_folder_exists(temp_dir):
    assert folder_exists(temp_dir.path) == True
    assert folder_exists(temp_dir.file1) == False


def test_clear_directory(temp_dir):
    import os
    full_dir_content_count = len(os.listdir(temp_dir.path))
    assert full_dir_content_count != 0
    clear_directory(temp_dir.path)
    empty_dir_content_count = len(os.listdir(temp_dir.path))
    assert empty_dir_content_count == 0


def test_is_file(temp_dir):
    assert _is_file(temp_dir.file1) == True
    assert _is_file(temp_dir.path) == False


def test_parse_markdown_file():
    # create (or use an already pre-existing) markdown file
    # with front matter content
    # make sure the function returns a tuple containing a dict
    # and a string
    # think about potentially failing cases (like if the file is empty)
    pass
