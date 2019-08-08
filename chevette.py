from colorama import Fore, Style
import os
import sys

ARTICLES_DIR = 'articles'
OUTPUT_DIR = 'public'


class Chevette(object):

    @classmethod
    def generate_boilerplate(cls, path):
        """
        create the basic folder structure necessary
        to the creation of a blog.
        /*
            articles -> where the blog posts will be stored (in markdown)
            public -> where the final site will be generated (in html)
        */
        """
        try:
            os.mkdir(path)
        except FileExistsError as e:
            err_msg = f"""
            [Error]: Could not create directory.
            Path ({e.filename}) Already Exists.
            Please make sure the directory is empty or use --force
            to overwrite the files.
            """
            print(Fore.RED + err_msg.strip())
            print(Style.RESET_ALL)
            sys.exit(1)
        else:
            os.mkdir(os.path.join(path, ARTICLES_DIR))
            os.mkdir(os.path.join(path, OUTPUT_DIR))
