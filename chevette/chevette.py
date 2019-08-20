import sys
import os
from colorama import Fore, Style
from chevette.constants import ARTICLES_DIR, OUTPUT_DIR
from chevette.article import Article
from shutil import copy2

from chevette.utils import (
    _is_file,
    _is_markdown,
    _is_extention_allowed,
    folder_exists,
    clear_directory,
    render_template_to_file
)


class Chevette(object):

    @classmethod
    def build(cls):
        # if there's no config file raise a cusom exception
        # if output dir exists clear it
        # gather all .md files and .html files and copy them over
        # copy all files over to /public and render the markdown files that you find

        # 1st copy over all files to /public
        if not folder_exists(OUTPUT_DIR):
            os.mkdir(os.path.join(os.getcwd(), OUTPUT_DIR))
        else:
            clear_directory(OUTPUT_DIR)

        other_files = cls._get_other_project_files()
        for file in other_files:
            copy2(file, OUTPUT_DIR)

        articles = cls._get_all_articles()

        for article in articles:
            article.parse()
            article.render()
            article.save_to_html()

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

            cls._print_error_and_exit(err_msg)

        else:
            cls._generate_boilerplate(path)

    @classmethod
    def _get_all_articles(cls, path=ARTICLES_DIR):
        return (
            Article(os.path.join(ARTICLES_DIR, article))
            for article in os.listdir(ARTICLES_DIR)
            if _is_file(os.path.join(ARTICLES_DIR, article))
            and _is_markdown(article)
        )

    @classmethod
    def _print_error_and_exit(cls, message):
        print(Fore.RED + message.strip())
        print(Style.RESET_ALL)
        sys.exit(1)

    @classmethod
    def _generate_boilerplate(cls, path):
        print('Generating default folder structure ...')
        if path != '.':
            os.mkdir(path)

        os.mkdir(os.path.join(path, ARTICLES_DIR))
        os.mkdir(os.path.join(path, OUTPUT_DIR))
        render_template_to_file(path, 'index.md')
        render_template_to_file(path, 'settings.py')
        print('Done !')

    @classmethod
    def _get_other_project_files(cls):
        cur_dir = os.getcwd()
        return (
           os.path.join(cur_dir, f) for f in os.listdir(cur_dir)
           if _is_file(os.path.join(cur_dir, f))
           and _is_extention_allowed(f)
        )
