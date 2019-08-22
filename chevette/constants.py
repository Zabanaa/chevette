from jinja2 import Environment, FileSystemLoader
import os

VERSION = '0.0.1'
TEMPLATES_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'templates'
)
ARTICLES_DIR = 'articles'
OUTPUT_DIR = 'public'
LAYOUTS_DIR = os.path.join(TEMPLATES_DIR, 'layouts')
THEME_DIR = os.path.join(os.getcwd(), 'theme')
THEME_JINJA_ENV = Environment(
    loader=FileSystemLoader(THEME_DIR),
    trim_blocks=True
)

EXTENSIONS_NOT_ALLOWED = (
    'py',
    'yml',
    'yaml'
    'toml'
    'ini',
    'php',
    'c',
    'cpp',
    'go',
    'lock',
    'json'
)