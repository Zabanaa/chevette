import os
import misaka as m
import frontmatter as fm
from chevette.constants import JINJA_ENV, OUTPUT_DIR


class Article(object):

    def __init__(self, path):
        self.path = path
        self.metadata = None
        self.content = None
        self.html = None

    def parse(self):
        _article = fm.load(self.path)
        self.metadata = _article.metadata
        self.content = _article.content

    def render(self):
        layout = self.metadata.get('layout', 'post')
        template = JINJA_ENV.get_template(f'layouts/{layout}.html.jinja2')
        self.html = template.render(
            content=m.html(self.content), **self.metadata
        )

    def save_to_html(self):
        with open(os.path.join(OUTPUT_DIR, self.html_filename), 'w') as f:
            f.write(self.html)

    @property
    def html_filename(self):
        return self.path.split('/')[1].split('.')[0] + '.html'