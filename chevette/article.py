import os
import misaka as m
import frontmatter as fm
from chevette.constants import OUTPUT_DIR, THEME_JINJA_ENV
from chevette.utils import folder_exists


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
        template = THEME_JINJA_ENV.get_template(f'{layout}.html.jinja2')
        self.html = template.render(
            content=m.html(self.content), **self.metadata
        )

    def save_to_html(self):
        public_articles_dir = os.path.join(OUTPUT_DIR, 'articles')
        public_article_path = os.path.join(
            public_articles_dir, self.html_filename
        )
        if not folder_exists(public_articles_dir):
            os.mkdir(public_articles_dir)

        with open(public_article_path, 'w') as f:
            f.write(self.html)

    @property
    def html_filename(self):
        return self.path.split('/')[1].split('.')[0] + '.html'
