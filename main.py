import os
import misaka
import frontmatter as fm
from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE_DIR = os.getcwd()
CONTENT_DIR = os.path.join(BASE_DIR, 'articles')
OUTPUT_DIR = os.path.join(BASE_DIR, 'public')
LAYOUTS_DIR = os.path.join(BASE_DIR, 'layouts')

env = Environment(
    loader=FileSystemLoader(LAYOUTS_DIR),
    autoescape=select_autoescape(['html', 'xml'])
)


def render_article(content, context_variables):
    layout = context_variables.get('layout', 'post')
    template = env.get_template(f'{layout}.html')
    return template.render(content=content, **context_variables)


def parse_article(file):
    post = fm.load(file)
    return (post.metadata, post.content)


def get_all_articles():

    return (
            f for f in os.listdir(CONTENT_DIR)
            if os.path.isfile(os.path.join(CONTENT_DIR, f))
            and f.endswith('.md')
            and not f.startswith('.')
        )


def create_public_directory():
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)


# TODO: break down the function below to only operate on a single file
def generate_html_from_markdown(files):
    for file in files:
        html_filename = file.split('.')[0] + '.html'
        with open(os.path.join(CONTENT_DIR, file), 'r') as f:
            # extract content and metadata from the file
            metadata, content = parse_article(f)
            new_entry = render_article(
                misaka.html(content),
                metadata
            )
            open(os.path.join(OUTPUT_DIR, html_filename), 'w').write(new_entry)


if __name__ == "__main__":
    create_public_directory()
    entries = get_all_articles()
    generate_html_from_markdown(entries)
