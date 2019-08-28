import os
import inspect
from importlib.machinery import SourceFileLoader
from chevette.exceptions import NoConfigError
from chevette.utils.constants import (
    ARTICLES_DIR,
    OUTPUT_DIR,
    TEMPLATES_DIR
)
from chevette.markdown import Page, Article
from shutil import copy2, copytree
from chevette.utils.helpers import (
    is_file,
    is_markdown,
    is_extention_allowed,
    folder_exists,
    clear_directory,
    print_error_and_exit,
)


class Chevette(object):

    @classmethod
    def build(cls):

        try:
            site_config = cls._load_config_file()
        except NoConfigError as e:
            print_error_and_exit(e.error_msg)

        cls._create_output_dir()

        other_files = cls._get_pages_and_other_files()

        for file in other_files:
            if is_markdown(file):
                page = Page(file)
                page.render_html(site_config)
            else:
                copy2(file, OUTPUT_DIR)

        articles = cls._get_all_articles()

        for article in articles:
            article.render_html(site_config)

    @classmethod
    def new(cls, path, force):
        """
        create the basic folder structure necessary
        to the creation of a blog.
        /*
            articles -> where the blog posts will be stored (in markdown)
            public -> where the final site will be generated (in html)
        */
        """

        if folder_exists(path) and path != '.':

            err_msg = f"""
            [Error]: Could not create directory.
            Path ({os.path.abspath(path)}) Already Exists.
            Please make sure the directory is empty or use --force
            to overwrite the files.
            """

            if force:
                print(f'Overwriting content inside {path}')
                clear_directory(path)
                print('Done !')
                return cls._generate_boilerplate(path)

            print_error_and_exit(err_msg)

        else:
            cls._generate_boilerplate(path)

    def _get_all_articles(path=ARTICLES_DIR):
        return (
            Article(os.path.abspath(os.path.join(ARTICLES_DIR, article)))
            for article in os.listdir(ARTICLES_DIR)
            if is_file(os.path.join(ARTICLES_DIR, article))
            and is_markdown(article)
        )

    def _generate_boilerplate(path):
        print('Generating default folder structure ...')

        if path != '.':
            os.mkdir(path)

        for fd in os.listdir(TEMPLATES_DIR):
            src = os.path.join(TEMPLATES_DIR, fd)
            if is_file(src):
                copy2(src, path)

            if folder_exists(src):
                dest = os.path.join(path, fd)
                copytree(src, dest)

        print('Done !')

    def _get_pages_and_other_files():
        cur_dir = os.getcwd()
        return (
           os.path.join(cur_dir, f) for f in os.listdir(cur_dir)
           if is_file(os.path.join(cur_dir, f))
           and is_extention_allowed(f)
        )

    def _create_output_dir():
        if not folder_exists(OUTPUT_DIR):
            os.mkdir(os.path.join(os.getcwd(), OUTPUT_DIR))
        else:
            clear_directory(OUTPUT_DIR)

    def _load_config_file():
        config_path = os.path.join(os.getcwd(), 'settings.py')
        if not is_file(config_path):
            raise NoConfigError
        else:
            config_module = SourceFileLoader('config', config_path).load_module()
            site_config = {'site': {}}
            config_settings = [
                (k.lower(), v) for k, v in inspect.getmembers(config_module)
                if k.isupper()
            ]
            site_config['site'].update(config_settings)
            return site_config
