import os
import misaka as m
import frontmatter as fm
from chevette.utils.constants import THEME_JINJA_ENV
from chevette.utils.helpers import print_error_and_exit
from jinja2.exceptions import TemplateNotFound


class MarkdownDocument(object):

    path = None
    is_page = False
    metadata = None
    content = None
    html_filename = None

    def _parse(self):
        _article = fm.load(self.path)
        self.metadata = _article.metadata
        self.content = _article.content

    def _render(self):
        layout = self.metadata.get('layout', 'post')
        try:
            template = THEME_JINJA_ENV.get_template(f'{layout}.html.jinja2')
        except TemplateNotFound as e:
            err_msg = f"""
            [Error]
            Unable to compile {self.path}.
            Could not find the following layout template: {e.name}.
            Make sure the spelling is correct or that a file named {e.name}
            sits under the theme directory.
            """
            print_error_and_exit(err_msg)
        else:
            self.html = template.render(
                content=m.html(self.content), **self.metadata
            )

    def render_html(self):
        self._parse()
        self._render()
        self._save_to_html()

    @property
    def html_filename(self):
        filename, _ = os.path.splitext(os.path.basename(self.path))
        return f'{filename}.html'
