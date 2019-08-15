from chevette.utils import (
    folder_exists,
    clear_directory,
    print_error_and_exit,
    _generate_boilerplate,
    _get_all_articles,
    _parse_article,
    _render_article,
    _save_article_to_html,
    _generate_html_filename
)


class Chevette(object):

    @classmethod
    def build(cls):
        # TODO: gather all html under os.getcwd() as well (but later)
        # for now just stick with /articles

        # 1. gather all .md files under /articles
        articles = _get_all_articles()

        for article in articles:
            # 2. parse them
            metadata, content = _parse_article(article)
            # 3. render them to html
            html_article = _render_article(content, metadata)
            new_filename = _generate_html_filename(article)

            # 4. save them to /public
            _save_article_to_html(html_article, new_filename)


    @classmethod
    def generate_boilerplate(cls, path, force):
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
            Path ({path}) Already Exists.
            Please make sure the directory is empty or use --force
            to overwrite the files.
            """

            if force:
                print(f'Overwriting content inside {path}')
                clear_directory(path)
                print('Done !')
                return _generate_boilerplate(path)

            print_error_and_exit(err_msg)

        else:
            _generate_boilerplate(path)
