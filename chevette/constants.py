import os
from jinja2 import Environment, FileSystemLoader

VERSION = '0.0.1'
TEMPLATES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'templates'
)
ARTICLES_DIR = 'articles'
OUTPUT_DIR = 'public'

JINJA_ENV = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    trim_blocks=True,
)

EXTENSIONS_NOT_ALLOWED = [
    'py',
    'yml',
    'yaml'
    'toml'
    'ini',
    'php',
    'c',
    'cpp',
    'go'
]