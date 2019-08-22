from chevette.utils import (
    _is_markdown,
    _is_extention_allowed,
    _get_html_filename
)
from chevette.constants import EXTENSIONS_NOT_ALLOWED


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


# for the following tests, you can simply create a bunch of fake directories
# with files, without having to resort to mocks, for some tests however you
# might have to use fixtures
# Lookup how pelican does it


def test_print_error_and_exit():
    # make sure sys.exit was called
    # make sure that print was called with the message
    pass


def test_folder_exists():
    # create a folder with some files in it
    # run the code against it
    # remove the folder afterwards
    pass


def test_clear_directory():
    # create a folder with some files in it
    # check the lenght of the content
    # call clear_directory against it
    # check the length again and make sure it's 0
    # remove the directory again
    pass


def test_is_file():
    # give a file path in test_data
    # run the code against it
    # try a failing case make sure it returns false
    pass


def test_parse_markdown_file():
    # create (or use an already pre-existing) markdown file
    # with front matter content
    # make sure the function returns a tuple containing a dict
    # and a string
    # think about potentially failing cases
    pass
