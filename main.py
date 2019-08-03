# step 1
# retrieve all entries inside /entries and parse them as markdown
# convert each one to html and save them to a different location.
import os
import misaka

BASE_DIR = os.getcwd()
CONTENT_DIR = os.path.join(BASE_DIR, 'entries')
OUTPUT_DIR = os.path.join(BASE_DIR, 'public')


def get_all_entries():

    fs = (
            f for f in os.listdir(CONTENT_DIR)
            if os.path.isfile(os.path.join(CONTENT_DIR, f))
            and f.endswith('.md')
            and not f.startswith('.')
        )
    return fs


def create_html_directory():
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)


def generate_html_from_markdown(files):
    for file in files:
        filename = file.split('.')[0]
        with open(os.path.join(CONTENT_DIR, file), 'r') as f:
            content = misaka.html(f.read())
            html_filename = filename + '.html'
            open(os.path.join(OUTPUT_DIR, html_filename), 'w').write(content)


if __name__ == "__main__":
    create_html_directory()
    entries = get_all_entries()
    generate_html_from_markdown(entries)
