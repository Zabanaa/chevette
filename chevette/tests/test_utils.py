from chevette.utils import _is_markdown


def test_is_markdown():
    assert _is_markdown('hello.md') == True
