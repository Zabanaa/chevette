from utils import (
    folder_exists,
    clear_directory,
    print_error_and_exit,
    _generate_boilerplate
)


class Chevette(object):

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

        if folder_exists(path):

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
